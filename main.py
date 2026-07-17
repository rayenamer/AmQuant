from __future__ import annotations

from amquant.loader import load_market_data


def main() -> None:
    result = load_market_data(
        fromdate="2009-01-01",
        todate="2026-06-01",
    )
    # RAW_SERIES / FEATURE_SETS are also mirrored into amquant.loader globals
    # by default, so nothing else to do here -- this file is just a dev
    # entrypoint to eyeball ok/failed/skipped counts before pushing.
    _ = result


if __name__ == "__main__":
    main()