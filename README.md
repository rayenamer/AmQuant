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

# Load market data for an explicit date range.
# fromdate / todate accept "YYYY-MM-DD" strings, date/datetime objects,
# or raw unix seconds.
result = amquant.load_market_data(
    fromdate="2024-01-01",
    todate="2024-06-01",
)

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

If `fromdate` / `todate` are omitted, `load_market_data()` defaults to a trailing 1-year window (today − 365 days → today).

## Downloading a Single Symbol

Every instrument in the universe is fetched through the same `download(what, fromdate, todate)` call under the hood. You can use it directly if you just want one symbol without going through the full universe/feature pipeline:

```python
from amquant.yahoo_finance import YahooFinanceClient

client = YahooFinanceClient()
series = client.download("AAPL", "2024-01-01", "2024-06-01")

print(series.symbol, len(series.bars))
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



# Contributing & Collaboration

AMQuant is an open-source project and welcomes contributions from developers, quantitative researchers, and Python enthusiasts.

## Getting Started

### 1. Fork the repository

Create your own fork of the AMQuant repository, then clone it locally:

```bash
git clone https://github.com/rayenamer/AmQuant
cd amquant
```

### 2. create a virtual environment

```bash
python3 -m venv venv

source venv/bin/activate
```

### 3. install development dependencies

```bash
python -m pip install --upgrade pip

pip install -e ".[dev]"
```

### 4. Write some good code (please keep the AI slop away)

# The Vision Behind AMQuant

AMQuant is designed as the data-engineering foundation of a quantitative research stack.