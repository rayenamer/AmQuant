**activate the virtual env with** :  source venv/bin/activate   

**interactive program** :python3 -i main.py

**DATA ACCESS:**

After `main()` executes in the same Python session:

- `RAW_SERIES: dict[str, Series]` — populated with fully enriched `Series` objects (OHLCV + metadata).
- `FEATURE_SETS: dict[str, FeatureSet]` — contains computed technical features per symbol.

Both dicts are module-level globals, accessible immediately post-run via `RAW_SERIES['BIAT']` or `FEATURE_SETS['MC']`.

Data lives in memory for the duration of the Python process / REPL session. Not persisted to disk unless explicitly saved.

For library use: expose `RAW_SERIES` and `FEATURE_SETS` via a `DataManager` singleton or return them from `load_universe()` for clean dependency injection.


# AmQuant
