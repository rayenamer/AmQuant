# AMQuant - Quick Start Guide

## Overview

**AMQuant** is an open-source Python library for quantitative finance that provides:

* Market data loading
* OHLCV time series management
* Feature engineering
* A clean Python API for research, backtesting and quantitative analysis

Unlike the original script-based implementation, AMQuant is now a fully installable Python package available through PyPI.

---

# 1. Create a Python Virtual Environment

It is recommended to work inside a virtual environment.

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
```

---

# 2. Install AMQuant

From PyPI

```bash
pip install amquant
```
# 3. Usage Example

```python
import amquant

# Load market data
result = amquant.load_market_data()

# Loading summary
print(f"Loaded : {result.ok}")
print(f"Failed : {result.failed}")
print(f"Skipped: {result.skipped}")

# Access raw market data
aapl_series = result.raw_series["AAPL"]

# Access engineered features
aapl_features = result.feature_sets["AAPL"]

# Alternatively, if update_globals=True (default)
aapl_series = amquant.RAW_SERIES["AAPL"]
aapl_features = amquant.FEATURE_SETS["AAPL"]
```

## Returned Object

`load_market_data()` returns a `LoadResult` dataclass containing both the loaded data and execution statistics.

| Attribute | Description |
|-----------|-------------|
| `result.raw_series` | Dictionary mapping `Symbol → Series` for successfully loaded instruments. |
| `result.feature_sets` | Dictionary mapping `Symbol → FeatureSet` containing the engineered features. |
| `result.ok` | Number of instruments successfully loaded and featurized. |
| `result.failed` | Number of instruments that failed during loading or feature computation. |
| `result.skipped` | Number of skipped instruments (missing or unavailable data). |

> **Note:** By default (`update_globals=True`), the loaded data is also mirrored into `amquant.RAW_SERIES` and `amquant.FEATURE_SETS` for interactive exploration in a Python REPL or Jupyter notebook. For production code, using `result.raw_series` and `result.feature_sets` is recommended.



# $$

AMQuant is designed as the data-engineering foundation of a quantitative research stack.

