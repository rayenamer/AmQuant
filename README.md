# quant-data-engine (Python port)

Direct Python equivalent of the C++ `quant-data-engine` project. Same file
breakdown, same funsction names, same hand-rolled math (Wilder smoothing for
RSI/ATR, same rolling-sum trick for SMA) -- verified numerically identical
on the same synthetic input: `RSI14[14]=85.7303, MACD[25]=2.00532` in both.

## File mapping

| C++ | Python | Role |
|---|---|---|
| `include/qde/bar.hpp` | `qde/bar.py` | `Bar` / `Series` dataclasses |
| `include/qde/http_client.*` | `qde/http_client.py` | HTTP GET wrapper (requests instead of libcurl) |
| `include/qde/yahoo_finance.*` | `qde/yahoo_finance.py` | Yahoo chart-API client |
| `include/qde/csv_io.*` | `qde/csv_io.py` | read/write CSV, source-agnostic |
| `include/qde/features.*` | `qde/features.py` | the 16 technical indicators |
| `include/qde/universe.*` | `qde/universe.py` | loads the 50-ticker list |
| `src/main.cpp` | `main.py` | runs the full pipeline |
| `tests/selftest.cpp` | `tests/selftest.py` | offline correctness check |

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
python3 tests/selftest.py      # sanity check, always works offline
python3 main.py                # full run, needs network for Yahoo-sourced names
```

Output lands in `data/raw/<SYMBOL>.csv` and `data/features/<SYMBOL>.csv`,
identical layout to the C++ version.

## The BVMT (Tunisian) gap

Same as the C++ version: Yahoo Finance doesn't carry Tunis Stock Exchange
listings. The 10 Tunisian rows in `data/universe.csv` (`source=manual_csv`)
need a matching file at `data/manual/<SYMBOL>.csv` with columns
`timestamp,open,high,low,close,adj_close,volume` (unix seconds), sourced
from bvmt.com.tn or ilboursa.com. `read_series_csv` doesn't care where the
file came from -- once it's in that shape, features compute identically.

## Why hand-rolled instead of pandas/ta-lib

This is a deliberate choice to keep the Python version a faithful mirror of
the C++ logic rather than a black box. If you don't need that parity and
just want less code, swap `features.py`'s internals for pandas:
`df['close'].rolling(20).mean()` replaces `_rolling_mean`, `df['close'].ewm(span=12).mean()`
replaces `_ema`, etc. -- the RSI/ATR Wilder smoothing is the one part
worth keeping hand-written even then, since `ta`-library RSI implementations
vary in their exact smoothing convention.



**activate the virtual env with** :  source venv/bin/activate   

**DATA ACCESS:**

After `main()` executes in the same Python session:

- `RAW_SERIES: dict[str, Series]` — populated with fully enriched `Series` objects (OHLCV + metadata).
- `FEATURE_SETS: dict[str, FeatureSet]` — contains computed technical features per symbol.

Both dicts are module-level globals, accessible immediately post-run via `RAW_SERIES['BIAT']` or `FEATURE_SETS['MC']`.

Data lives in memory for the duration of the Python process / REPL session. Not persisted to disk unless explicitly saved.

For library use: expose `RAW_SERIES` and `FEATURE_SETS` via a `DataManager` singleton or return them from `load_universe()` for clean dependency injection.

# AmQuant
