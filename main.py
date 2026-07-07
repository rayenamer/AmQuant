from __future__ import annotations
import sys
import time

from qde.universe_data import UNIVERSE
from qde.manual_data import MANUAL_SERIES
from qde.yahoo_finance import YahooFinanceClient
from qde.features import compute_features, FeatureSet
from qde.bar import Series

RAW_SERIES: dict[str, Series] = {}
FEATURE_SETS: dict[str, FeatureSet] = {}


def main() -> None:
    universe = UNIVERSE
    print(f"Loaded {len(universe)} instruments")

    yahoo = YahooFinanceClient()
    ok = failed = skipped = 0

    for inst in universe:
        series = None
        if inst.source == "yahoo" and inst.yahoo_symbol:
            series = yahoo.fetch_history(inst.yahoo_symbol, "1y", "1d")
            time.sleep(0.3)  # me being polite and waiting between calls :3
        else:
            series = MANUAL_SERIES.get(inst.symbol)
            if series is None:
                print(f"[manual] {inst.symbol}: no entry in MANUAL_SERIES", file=sys.stderr)

        if not series or not series.bars:
            print(f"SKIP  {inst.symbol} ({inst.exchange})", file=sys.stderr)
            skipped += 1
            continue

        series.symbol = inst.symbol
        series.exchange = inst.exchange
        series.country = inst.country

        try:
            features = compute_features(series)

            RAW_SERIES[inst.symbol] = series
            FEATURE_SETS[inst.symbol] = features

            print(f"OK    {inst.symbol} ({inst.exchange}) -- {len(series.bars)} bars")
            ok += 1
        except Exception as e:
            print(f"FAIL  {inst.symbol}: {e}", file=sys.stderr)
            failed += 1

    print(f"\nDone. ok={ok} failed={failed} skipped={skipped}")


if __name__ == "__main__":
    main()