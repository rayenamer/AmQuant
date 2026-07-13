**activate the virtual env with** :  source venv/bin/activate   

**interactive program** :python3 -i main.py

**DATA ACCESS:**

After `main()` executes in the same Python session:

- `RAW_SERIES: dict[str, Series]` — populated with fully enriched `Series` objects (OHLCV + metadata).
- `FEATURE_SETS: dict[str, FeatureSet]` — contains computed technical features per symbol.

Both dicts are module-level globals, accessible immediately post-run via `RAW_SERIES['BIAT']` or `FEATURE_SETS['MC']`.

Data lives in memory for the duration of the Python process / REPL session. Not persisted to disk unless explicitly saved.

For library use: expose `RAW_SERIES` and `FEATURE_SETS` via a `DataManager` singleton or return them from `load_universe()` for clean dependency injection.

**demo**

list(RAW_SERIES.keys())
RAW_SERIES["BNP"].bars[0]
FEATURE_SETS["BNP"].ret_1d[:5]
FEATURE_SETS["BNP"].sma_20[:5]
FEATURE_SETS["BNP"].__dict__.keys()
len(RAW_SERIES["BNP"].bars)
len(RAW_SERIES)
len(FEATURE_SETS)

# AmQuant
