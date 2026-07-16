"""Yahoo Finance ingestion. Mirrors include/qde/yahoo_finance.hpp + src/yahoo_finance.cpp.

Uses the same unofficial chart endpoint:
    https://query1.finance.yahoo.com/v8/finance/chart/<symbol>

NOTE: Tunis Stock Exchange (BVMT) tickers are NOT covered by Yahoo Finance --
same caveat as the C++ version. Use csv_io.read_series_csv for those instead.
"""
from __future__ import annotations
import sys
import datetime as dt
from typing import Optional, Union

from amquant.dataDefinitions.bar import Bar, Series
from amquant.dataInra.http_client import HttpClient

_INTERVAL_MAP = {"1d": "1d", "1wk": "1wk", "1mo": "1mo"}

DateLike = Union[int, str, dt.date, dt.datetime]


def _to_unix(value: DateLike) -> int:
    """Normalize from_/to into unix seconds (UTC).

    Accepts:
      - int / float          -> already unix seconds, passed through
      - "YYYY-MM-DD" string  -> parsed as UTC midnight
      - datetime.date        -> UTC midnight of that date
      - datetime.datetime    -> converted to UTC if naive/aware
    """
    if isinstance(value, bool):
        raise TypeError("bool is not a valid date")
    if isinstance(value, (int, float)):
        return int(value)
    if isinstance(value, str):
        parsed = dt.datetime.strptime(value, "%Y-%m-%d")
        return int(parsed.replace(tzinfo=dt.timezone.utc).timestamp())
    if isinstance(value, dt.datetime):
        if value.tzinfo is None:
            value = value.replace(tzinfo=dt.timezone.utc)
        return int(value.timestamp())
    if isinstance(value, dt.date):
        combined = dt.datetime.combine(value, dt.time.min, tzinfo=dt.timezone.utc)
        return int(combined.timestamp())
    raise TypeError(f"unsupported date type for from_/to: {type(value)!r}")


class YahooFinanceClient:
    """Equivalent of qde::YahooFinanceClient."""

    def __init__(self, http_client: HttpClient | None = None):
        self.http = http_client or HttpClient()

    def download(
        self,
        what: str,
        fromdate: DateLike,
        todate: DateLike,
        interval: str = "1d",
    ) -> Optional[Series]:
        """The one download entry point every caller (loader.py, ad-hoc
        scripts, etc.) should go through.

        what     -- Yahoo ticker, e.g. 'AAPL', 'MC.PA', 'SAP.DE'
        fromdate -- start of range (date string 'YYYY-MM-DD', date/datetime, or unix seconds)
        todate   -- end of range (same accepted types as fromdate)
        interval -- bar size, one of _INTERVAL_MAP

        Returns None on failure (network, bad HTTP status, bad JSON), same
        fail-soft behaviour as the C++ version so one bad symbol doesn't
        kill a batch run.
        """
        try:
            period1 = _to_unix(fromdate)
            period2 = _to_unix(todate)
        except (TypeError, ValueError) as e:
            print(f"[yahoo] bad fromdate/todate for {what}: {e}", file=sys.stderr)
            return None

        if period1 >= period2:
            print(f"[yahoo] fromdate must be before todate for {what} ({period1} >= {period2})", file=sys.stderr)
            return None

        url = (
            f"https://query1.finance.yahoo.com/v8/finance/chart/{what}"
            f"?period1={period1}&period2={period2}"
            f"&interval={_INTERVAL_MAP.get(interval, '1d')}"
            f"&events=div,splits"
        )
        try:
            resp = self.http.get(url, headers={"Accept": "application/json"})
        except RuntimeError as e:
            print(f"[yahoo] request failed for {what}: {e}", file=sys.stderr)
            return None

        if not resp.ok():
            print(f"[yahoo] HTTP {resp.status_code} for {what}", file=sys.stderr)
            return None

        return self._parse_chart_json(what, resp.body)

    def _parse_chart_json(self, symbol: str, json_text: str) -> Optional[Series]:
        import json as jsonlib
        try:
            root = jsonlib.loads(json_text)
            result = root["chart"]["result"]
            if not result:
                print(f"[yahoo] empty result for {symbol}", file=sys.stderr)
                return None
            r0 = result[0]
            timestamps = r0["timestamp"]
            quote = r0["indicators"]["quote"][0]
            opens, highs, lows, closes, volumes = (
                quote["open"], quote["high"], quote["low"], quote["close"], quote["volume"],
            )
            adjclose = None
            if "adjclose" in r0["indicators"]:
                adjclose = r0["indicators"]["adjclose"][0]["adjclose"]

            series = Series(symbol=symbol)
            for i, ts in enumerate(timestamps):
                if ts is None or closes[i] is None:
                    continue  # skip holes, same as the C++ version
                bar = Bar(
                    timestamp_utc=int(ts),
                    open=opens[i] or 0.0,
                    high=highs[i] or 0.0,
                    low=lows[i] or 0.0,
                    close=closes[i],
                    volume=volumes[i] or 0.0,
                    adj_close=(adjclose[i] if adjclose and adjclose[i] is not None else closes[i]),
                )
                series.bars.append(bar)
            return series
        except (KeyError, IndexError, TypeError, ValueError, jsonlib.JSONDecodeError) as e:
            print(f"[yahoo] JSON parse error for {symbol}: {e}", file=sys.stderr)
            return None