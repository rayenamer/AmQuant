from __future__ import annotations
import sys
import time
import datetime as dt
from dataclasses import dataclass, field

from amquant.dataDefinitions.universe_data import UNIVERSE
from amquant.dataSources.yahoo_finance import YahooFinanceClient, DateLike
from amquant.dataDefinitions.features import compute_features, FeatureSet
from amquant.dataDefinitions.bar import Series

RAW_SERIES: dict[str, Series] = {}
FEATURE_SETS: dict[str, FeatureSet] = {}


@dataclass
class LoadResult:
    raw_series: dict[str, Series] = field(default_factory=dict)
    feature_sets: dict[str, FeatureSet] = field(default_factory=dict)
    ok: int = 0
    failed: int = 0
    skipped: int = 0


def load_market_data(
    universe=None,
    *,
    yahoo_client: YahooFinanceClient | None = None,
    fromdate: DateLike | None = None,
    todate: DateLike | None = None,
    sleep_between_calls: float = 0.3,
    verbose: bool = True,
    update_globals: bool = True,
) -> LoadResult:
    """
    Fetch/assemble bar series for every instrument in `universe`, compute features,
    and return them as a LoadResult. By default also mirrors results into
    amquant.loader.RAW_SERIES / FEATURE_SETS for quick terminal inspection.

    fromdate / todate default to a 1y trailing window (today - 365d .. today)
    if not given, and are computed once here so every instrument requests the
    exact same window through the same yahoo.download(what, fromdate, todate) call.
    """
    universe = universe if universe is not None else UNIVERSE
    yahoo = yahoo_client if yahoo_client is not None else YahooFinanceClient()

    todate_ = todate if todate is not None else dt.datetime.now(dt.timezone.utc)
    fromdate_ = fromdate if fromdate is not None else todate_ - dt.timedelta(days=365)

    result = LoadResult()

    if verbose:
        print(f"Loaded {len(universe)} instruments")

    for inst in universe:
        series = None
        if inst.source == "yahoo" and inst.yahoo_symbol:
            series = yahoo.download(inst.yahoo_symbol, fromdate_, todate_)
            if sleep_between_calls:
                time.sleep(sleep_between_calls)
        else:
            if series is None and verbose:
                print(f"[manual] {inst.symbol}: no entry in MANUAL_SERIES", file=sys.stderr)

        if not series or not series.bars:
            if verbose:
                print(f"SKIP  {inst.symbol} ({inst.exchange})", file=sys.stderr)
            result.skipped += 1
            continue

        series.symbol = inst.symbol
        series.exchange = inst.exchange
        series.country = inst.country

        try:
            features = compute_features(series)
            result.raw_series[inst.symbol] = series
            result.feature_sets[inst.symbol] = features
            if verbose:
                print(f"OK    {inst.symbol} ({inst.exchange}) -- {len(series.bars)} bars")
            result.ok += 1
        except Exception as e:
            if verbose:
                print(f"FAIL  {inst.symbol}: {e}", file=sys.stderr)
            result.failed += 1

    if verbose:
        print(f"\nDone. ok={result.ok} failed={result.failed} skipped={result.skipped}")

    if update_globals:
        RAW_SERIES.clear()
        RAW_SERIES.update(result.raw_series)
        FEATURE_SETS.clear()
        FEATURE_SETS.update(result.feature_sets)

    return result