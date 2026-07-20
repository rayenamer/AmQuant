from __future__ import annotations
import math
import datetime as dt
from dataclasses import dataclass, field
from amquant.dataDefinitions.bar import Series

NaN = float("nan")


@dataclass
class FeatureSet:
    """All lists are the same length as series.bars. Early entries in any
    rolling-window feature are NaN until the window fills."""

    # Timestamps
    timestamp: list = field(default_factory=list)

    # === Returns & Price Transformations ===
    ret_1d: list = field(default_factory=list)           # 1. Simple return
    log_ret_1d: list = field(default_factory=list)       # 1. Log return (single-period)
    log_ret_5d: list = field(default_factory=list)       # multi-period
    log_ret_20d: list = field(default_factory=list)
    cum_ret_5d: list = field(default_factory=list)       # 2. Cumulative returns
    cum_ret_10d: list = field(default_factory=list)
    cum_ret_20d: list = field(default_factory=list)
    cum_ret_60d: list = field(default_factory=list)
    price_vs_sma_20: list = field(default_factory=list)  # 3. (Close - SMA)/SMA
    roc_10: list = field(default_factory=list)           # 4. Rate of Change
    roc_20: list = field(default_factory=list)

    # === Volatility ===
    vol_20: list = field(default_factory=list)           # 5. Historical vol (annualized)
    atr_14: list = field(default_factory=list)           # 6. ATR
    bb_width_20: list = field(default_factory=list)      # 7. Bollinger Band width
    bb_percent_b: list = field(default_factory=list)     # 7. %B
    # GARCH (8) omitted — too heavy for pure Python without scipy/optim; use external lib if needed

    # === Momentum & Trend ===
    rsi_14: list = field(default_factory=list)           # 9.
    macd: list = field(default_factory=list)             # 10.
    macd_hist: list = field(default_factory=list)        # 10. MACD histogram
    adx_14: list = field(default_factory=list)           # 11. (simplified)
    stoch_k_14: list = field(default_factory=list)       # 12.
    stoch_d_3: list = field(default_factory=list)

    # === Volume-Based ===
    obv: list = field(default_factory=list)              # 13.
    vwap_dev: list = field(default_factory=list)         # 14. (Close - VWAP)/VWAP
    volume_zscore_20: list = field(default_factory=list) # 15.

    # === Lag & Statistical ===
    ret_lag_1: list = field(default_factory=list)        # 16.
    ret_lag_5: list = field(default_factory=list)
    ret_lag_10: list = field(default_factory=list)
    skew_20: list = field(default_factory=list)          # 17.
    kurt_20: list = field(default_factory=list)
    autocorr_20: list = field(default_factory=list)      # 18. (simple lag-1 autocorr over window)

    # === Cross-Asset & Contextual (requires benchmark series) ===
    # Pass a benchmark Series to compute_features if you want these
    rel_strength: list = field(default_factory=list)     # 19.
    beta_20: list = field(default_factory=list)          # 20. rolling beta

    # Bonus
    day_of_week: list = field(default_factory=list)


def _rolling_mean(x: list, window: int) -> list:
    out = [NaN] * len(x)
    s = 0.0
    for i, v in enumerate(x):
        s += v
        if i >= window:
            s -= x[i - window]
        if i >= window - 1:
            out[i] = s / window
    return out


def _rolling_std(x: list, window: int) -> list:
    out = [NaN] * len(x)
    for i in range(window - 1, len(x)):
        window_vals = x[i - window + 1: i + 1]
        mean = sum(window_vals) / window
        var = sum((v - mean) ** 2 for v in window_vals) / max(window - 1, 1)
        out[i] = math.sqrt(var)
    return out


def _ema(x: list, window: int) -> list:
    out = [NaN] * len(x)
    if not x:
        return out
    alpha = 2.0 / (window + 1.0)
    prev = NaN
    for i, v in enumerate(x):
        if math.isnan(v):
            out[i] = prev
            continue
        prev = v if math.isnan(prev) else alpha * v + (1 - alpha) * prev
        out[i] = prev
    return out


def _true_range(high: list, low: list, close: list) -> list:
    n = len(high)
    tr = [NaN] * n
    for i in range(1, n):
        a = high[i] - low[i]
        b = abs(high[i] - close[i - 1])
        c = abs(low[i] - close[i - 1])
        tr[i] = max(a, b, c)
    return tr


def compute_features(series: Series, benchmark: Series | None = None) -> FeatureSet:
    bars = series.bars
    n = len(bars)
    f = FeatureSet()
    f.timestamp = [b.timestamp_utc for b in bars]

    close = [b.adj_close if getattr(b, 'adj_close', 0) != 0 else b.close for b in bars]
    high = [b.high for b in bars]
    low = [b.low for b in bars]
    volume = [b.volume for b in bars]

    # === Returns & Price Transformations ===
    f.ret_1d = [NaN] * n
    f.log_ret_1d = [NaN] * n
    for i in range(1, n):
        if close[i - 1] > 0:
            f.ret_1d[i] = close[i] / close[i - 1] - 1.0
            f.log_ret_1d[i] = math.log(close[i] / close[i - 1])

    # Multi-period log returns & cumulative
    for period in [5, 20]:
        attr = f"log_ret_{period}d"
        setattr(f, attr, [NaN] * n)
        for i in range(period, n):
            if close[i - period] > 0:
                getattr(f, attr)[i] = math.log(close[i] / close[i - period])

    for period in [5, 10, 20, 60]:
        attr = f"cum_ret_{period}d"
        setattr(f, attr, [NaN] * n)
        for i in range(period, n):
            if close[i - period] > 0:
                getattr(f, attr)[i] = close[i] / close[i - period] - 1.0

    sma_20 = _rolling_mean(close, 20)
    for i in range(n):
        f.price_vs_sma_20.append(NaN if math.isnan(sma_20[i]) or sma_20[i] == 0 else
                                 (close[i] - sma_20[i]) / sma_20[i])

    for period in [10, 20]:
        attr = f"roc_{period}"
        setattr(f, attr, [NaN] * n)
        for i in range(period, n):
            if close[i - period] > 0:
                getattr(f, attr)[i] = (close[i] / close[i - period] - 1.0) * 100

    # === Volatility ===
    f.vol_20 = _rolling_std(f.log_ret_1d, 20)
    f.vol_20 = [v * math.sqrt(252.0) if not math.isnan(v) else v for v in f.vol_20]

    f.atr_14 = [NaN] * n
    tr = _true_range(high, low, close)
    atr = 0.0
    window = 14
    for i in range(1, n):
        if i <= window:
            atr += tr[i] / window
            if i == window:
                f.atr_14[i] = atr
        else:
            atr = (atr * (window - 1) + tr[i]) / window
            f.atr_14[i] = atr

    # Bollinger
    std_20 = _rolling_std(close, 20)
    f.bb_width_20 = [NaN] * n
    f.bb_percent_b = [NaN] * n
    for i in range(n):
        if not math.isnan(sma_20[i]) and not math.isnan(std_20[i]):
            upper = sma_20[i] + 2 * std_20[i]
            lower = sma_20[i] - 2 * std_20[i]
            f.bb_width_20[i] = (upper - lower) / sma_20[i] if sma_20[i] != 0 else NaN
            f.bb_percent_b[i] = (close[i] - lower) / (upper - lower) if (upper - lower) != 0 else NaN

    # === Momentum & Trend ===
    # RSI (already good in your original)
    f.rsi_14 = [NaN] * n
    window = 14
    avg_gain = avg_loss = 0.0
    for i in range(1, n):
        change = close[i] - close[i - 1]
        gain = max(change, 0)
        loss = max(-change, 0)
        if i <= window:
            avg_gain += gain / window
            avg_loss += loss / window
            if i == window:
                rs = float('inf') if avg_loss == 0 else avg_gain / avg_loss
                f.rsi_14[i] = 100 - (100 / (1 + rs))
        else:
            avg_gain = (avg_gain * (window - 1) + gain) / window
            avg_loss = (avg_loss * (window - 1) + loss) / window
            rs = float('inf') if avg_loss == 0 else avg_gain / avg_loss
            f.rsi_14[i] = 100 - (100 / (1 + rs))

    # MACD + histogram
    ema12 = _ema(close, 12)
    ema26 = _ema(close, 26)
    f.macd = [NaN if math.isnan(ema12[i]) or math.isnan(ema26[i]) else ema12[i] - ema26[i] for i in range(n)]
    macd_signal = _ema(f.macd, 9)
    f.macd_hist = [NaN if math.isnan(f.macd[i]) or math.isnan(macd_signal[i]) else f.macd[i] - macd_signal[i] for i in range(n)]

    # Simplified ADX (DI+/DI- based)
    f.adx_14 = [NaN] * n  # placeholder — full Wilder ADX is lengthy; expand if needed

    # Stochastic
    f.stoch_k_14 = [NaN] * n
    f.stoch_d_3 = [NaN] * n
    for i in range(14, n):
        hh = max(high[i-13:i+1])
        ll = min(low[i-13:i+1])
        if hh != ll:
            f.stoch_k_14[i] = (close[i] - ll) / (hh - ll) * 100
    f.stoch_d_3 = _rolling_mean(f.stoch_k_14, 3)

    # === Volume ===
    f.obv = [NaN] * n
    f.obv[0] = 0
    for i in range(1, n):
        if close[i] > close[i-1]:
            f.obv[i] = f.obv[i-1] + volume[i]
        elif close[i] < close[i-1]:
            f.obv[i] = f.obv[i-1] - volume[i]
        else:
            f.obv[i] = f.obv[i-1]

    # VWAP (cumulative for the whole series — adjust if you want rolling)
    cum_pv = [0.0] * n
    cum_vol = [0.0] * n
    for i in range(n):
        typical_price = (high[i] + low[i] + close[i]) / 3
        cum_pv[i] = cum_pv[i-1] + typical_price * volume[i] if i > 0 else typical_price * volume[i]
        cum_vol[i] = cum_vol[i-1] + volume[i] if i > 0 else volume[i]
        f.vwap_dev.append(NaN if cum_vol[i] == 0 else (close[i] - cum_pv[i]/cum_vol[i]) / (cum_pv[i]/cum_vol[i]))

    vol_mean_20 = _rolling_mean(volume, 20)
    vol_std_20 = _rolling_std(volume, 20)
    f.volume_zscore_20 = [NaN] * n
    for i in range(n):
        if not math.isnan(vol_mean_20[i]) and not math.isnan(vol_std_20[i]) and vol_std_20[i] > 0:
            f.volume_zscore_20[i] = (volume[i] - vol_mean_20[i]) / vol_std_20[i]

    # === Lag & Statistical ===
    f.ret_lag_1 = f.ret_1d[:]
    f.ret_lag_5 = [NaN] * n
    f.ret_lag_10 = [NaN] * n
    for i in range(5, n):
        f.ret_lag_5[i] = f.ret_1d[i-5]
    for i in range(10, n):
        f.ret_lag_10[i] = f.ret_1d[i-10]

    # Skew & Kurtosis (simple)
    for i in range(20, n):
        w = f.log_ret_1d[i-19:i+1]
        mean = sum(w)/20
        # w is a 20-item window; compute variance/std directly to avoid
        # indexing into a short _rolling_std(...) result with the
        # absolute index `i` (which causes IndexError).
        var = sum((v - mean) ** 2 for v in w) / max(20 - 1, 1)
        std = math.sqrt(var)
        if std > 0:
            skew = sum(((v - mean)/std)**3 for v in w) / 20
            kurt = sum(((v - mean)/std)**4 for v in w) / 20 - 3
            f.skew_20.append(skew)
            f.kurt_20.append(kurt)
        else:
            f.skew_20.append(NaN)
            f.kurt_20.append(NaN)
    # pad beginning
    f.skew_20 = [NaN]*20 + f.skew_20
    f.kurt_20 = [NaN]*20 + f.kurt_20

    # Simple autocorrelation (lag-1 over 20d window)
    f.autocorr_20 = [NaN] * n
    for i in range(20, n):
        w = f.log_ret_1d[i-19:i+1]
        mean = sum(w)/20
        cov = sum((w[j]-mean)*(w[j-1]-mean) for j in range(1,20)) / 19
        var = sum((v-mean)**2 for v in w)/19
        f.autocorr_20[i] = cov / var if var > 0 else NaN

    # === Cross-Asset (if benchmark provided) ===
    if benchmark:
        bench_close = [b.adj_close if getattr(b, 'adj_close', 0) != 0 else b.close for b in benchmark.bars]
        # assume same length for simplicity
        bench_ret = [NaN] * n
        for i in range(1, n):
            if bench_close[i-1] > 0:
                bench_ret[i] = bench_close[i]/bench_close[i-1] - 1
        f.rel_strength = [NaN if math.isnan(f.ret_1d[i]) or math.isnan(bench_ret[i]) else f.ret_1d[i] - bench_ret[i] for i in range(n)]
        # rolling beta (cov / var_bench)
        # ... implement similarly to autocorrelation if needed

    # Bonus
    # `Bar.timestamp_utc` is stored as UNIX seconds (int). Convert to
    # timezone-aware datetime before calling `weekday()`; tolerate
    # unexpected types by falling back to NaN.
    f.day_of_week = []
    for b in bars:
        ts = getattr(b, 'timestamp_utc', None)
        if isinstance(ts, (int, float)):
            try:
                d = dt.datetime.fromtimestamp(ts, dt.timezone.utc)
                f.day_of_week.append(d.weekday())
                continue
            except Exception:
                pass
        if hasattr(ts, 'weekday'):
            try:
                f.day_of_week.append(ts.weekday())
                continue
            except Exception:
                pass
        f.day_of_week.append(NaN)

    return f




# ====================== FEATURE DESCRIPTIONS ======================

FEATURE_DESCRIPTIONS = {
    "ret_1d": "Daily simple return: (Close_t / Close_{t-1}) - 1",
    "log_ret_1d": "Daily log return: log(Close_t / Close_{t-1})",
    "log_ret_5d": "5-day log return",
    "log_ret_20d": "20-day log return",
    "cum_ret_5d": "Cumulative simple return over rolling 5-day window",
    "cum_ret_10d": "Cumulative simple return over rolling 10-day window",
    "cum_ret_20d": "Cumulative simple return over rolling 20-day window",
    "cum_ret_60d": "Cumulative simple return over rolling 60-day window",
    "price_vs_sma_20": "Price relative to 20-day SMA: (Close - SMA_20) / SMA_20",
    "roc_10": "Rate of Change (10-day) in percent",
    "roc_20": "Rate of Change (20-day) in percent",

    "vol_20": "20-day historical volatility (annualized std of log returns)",
    "atr_14": "14-day Average True Range using Wilder smoothing",
    "bb_width_20": "Bollinger Bands (20,2) width normalized by middle band",
    "bb_percent_b": "Bollinger %B — where price sits inside the bands (0 to 1)",

    "rsi_14": "14-day Relative Strength Index (momentum oscillator)",
    "macd": "MACD line: EMA12 - EMA26",
    "macd_hist": "MACD Histogram: MACD line - Signal line (EMA9)",
    "adx_14": "Average Directional Index (trend strength)",
    "stoch_k_14": "Stochastic %K (14-period fast)",
    "stoch_d_3": "Stochastic %D (3-period SMA of %K)",

    "obv": "On-Balance Volume — cumulative volume pressure",
    "vwap_dev": "Deviation from Volume-Weighted Average Price",
    "volume_zscore_20": "Volume z-score relative to 20-day mean and std",

    "ret_lag_1": "1-period lagged daily return",
    "ret_lag_5": "5-period lagged daily return",
    "ret_lag_10": "10-period lagged daily return",
    "skew_20": "Rolling 20-day skewness of log returns",
    "kurt_20": "Rolling 20-day excess kurtosis of log returns",
    "autocorr_20": "Rolling 20-day lag-1 autocorrelation of log returns",

    "rel_strength": "Relative strength vs benchmark (stock return - benchmark return)",
    "beta_20": "Rolling 20-day beta vs benchmark index",

    "day_of_week": "Day of the week (0 = Monday, 6 = Sunday)",
}


def describe(feature: str) -> str:
    """
    Get a human-readable description of any feature.
    
    Example:
        describe("macd_hist") 
        → "MACD Histogram: MACD line - Signal line (EMA9)"
    """
    desc = FEATURE_DESCRIPTIONS.get(feature)
    if desc:
        return desc
    
    # Fuzzy search help
    matches = [k for k in FEATURE_DESCRIPTIONS if feature.lower() in k.lower()]
    if matches:
        return f"Feature '{feature}' not found. Did you mean: {', '.join(matches[:5])}?"
    return f"Unknown feature: '{feature}'"


def list_features() -> list[str]:
    """Return sorted list of all available feature names."""
    return sorted(FEATURE_DESCRIPTIONS.keys())


def feature_summary() -> None:
    """Print a nice overview of all features."""
    print("=== Available Features ===\n")
    for name in list_features():
        print(f"{name:18} : {describe(name)}")