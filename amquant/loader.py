from __future__ import annotations
import sys
import time
from dataclasses import dataclass, field

from amquant.universe_data import UNIVERSE
from amquant.manual_data import MANUAL_SERIES
from amquant.yahoo_finance import YahooFinanceClient
from amquant.features import compute_features, FeatureSet
from amquant.bar import Series

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
    sleep_between_calls: float = 0.3,
    verbose: bool = True,
    update_globals: bool = True,
) -> LoadResult:
    """
    Fetch/assemble bar series for every instrument in `universe`, compute features,
    and return them as a LoadResult. By default also mirrors results into
    amquant.loader.RAW_SERIES / FEATURE_SETS for quick terminal inspection.
    """
    universe = universe if universe is not None else UNIVERSE
    yahoo = yahoo_client if yahoo_client is not None else YahooFinanceClient()

    result = LoadResult()

    if verbose:
        print(f"Loaded {len(universe)} instruments")

    for inst in universe:
        series = None
        if inst.source == "yahoo" and inst.yahoo_symbol:
            series = yahoo.fetch_history(inst.yahoo_symbol, "1y", "1d")
            if sleep_between_calls:
                time.sleep(sleep_between_calls)
        else:
            series = MANUAL_SERIES.get(inst.symbol)
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