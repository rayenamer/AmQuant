"""Yahoo Finance ingestion. Mirrors include/qde/yahoo_finance.hpp + src/yahoo_finance.cpp.

Uses the same unofficial chart endpoint:
    https://query1.finance.yahoo.com/v8/finance/chart/<symbol>

NOTE: Tunis Stock Exchange (BVMT) tickers are NOT covered by Yahoo Finance --
same caveat as the C++ version. Use csv_io.read_series_csv for those instead.
"""
from __future__ import annotations
import sys
from typing import Optional

from qde.bar import Bar, Series
from qde.http_client import HttpClient

_RANGE_MAP = {
    "5d": "5d", "1mo": "1mo", "3mo": "3mo", "6mo": "6mo",
    "1y": "1y", "2y": "2y", "5y": "5y", "10y": "10y", "max": "max",
}
_INTERVAL_MAP = {"1d": "1d", "1wk": "1wk", "1mo": "1mo"}


class YahooFinanceClient:
    """Equivalent of qde::YahooFinanceClient."""

    def __init__(self, http_client: HttpClient | None = None):
        self.http = http_client or HttpClient()

    def fetch_history(self, symbol: str, range_: str = "2y", interval: str = "1d") -> Optional[Series]:
        """symbol must be the Yahoo ticker, e.g. 'AAPL', 'MC.PA', 'SAP.DE'.
        Returns None on failure (network or bad HTTP status), same fail-soft
        behaviour as the C++ version so one bad symbol doesn't kill a batch run.
        """
        url = (
            f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
            f"?range={_RANGE_MAP.get(range_, '2y')}"
            f"&interval={_INTERVAL_MAP.get(interval, '1d')}"
            f"&events=div,splits"
        )
        try:
            resp = self.http.get(url, headers={"Accept": "application/json"})
        except RuntimeError as e:
            print(f"[yahoo] request failed for {symbol}: {e}", file=sys.stderr)
            return None

        if not resp.ok():
            print(f"[yahoo] HTTP {resp.status_code} for {symbol}", file=sys.stderr)
            return None

        return self._parse_chart_json(symbol, resp.body)

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
