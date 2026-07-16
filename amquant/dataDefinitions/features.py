"""Feature engineering. Mirrors include/qde/features.hpp + src/features.cpp.

Deliberately hand-rolled (not pandas/ta-lib) so the math is a line-for-line
match with the C++ version -- same Wilder smoothing for RSI/ATR, same
rolling-sum trick for the moving average, same annualization factor.
"""
from __future__ import annotations
import math
from dataclasses import dataclass, field

from amquant.dataDefinitions.bar import Series

NaN = float("nan")


@dataclass
class FeatureSet:
    """All lists are the same length as series.bars. Early entries in any
    rolling-window feature are NaN until the window fills."""
    timestamp: list = field(default_factory=list)
    ret_1d: list = field(default_factory=list)
    log_ret_1d: list = field(default_factory=list)
    sma_5: list = field(default_factory=list)
    sma_20: list = field(default_factory=list)
    sma_50: list = field(default_factory=list)
    ema_12: list = field(default_factory=list)
    ema_26: list = field(default_factory=list)
    macd: list = field(default_factory=list)
    macd_signal: list = field(default_factory=list)
    rsi_14: list = field(default_factory=list)
    vol_20: list = field(default_factory=list)
    bb_upper_20: list = field(default_factory=list)
    bb_lower_20: list = field(default_factory=list)
    atr_14: list = field(default_factory=list)
    momentum_10: list = field(default_factory=list)
    volume_zscore_20: list = field(default_factory=list)


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


def compute_features(series: Series) -> FeatureSet:
    bars = series.bars
    n = len(bars)
    f = FeatureSet()
    f.timestamp = [b.timestamp_utc for b in bars]

    close = [b.adj_close if b.adj_close != 0.0 else b.close for b in bars]
    volume = [b.volume for b in bars]
    high = [b.high for b in bars]
    low = [b.low for b in bars]

    f.ret_1d = [NaN] * n
    f.log_ret_1d = [NaN] * n
    for i in range(1, n):
        if close[i - 1] > 0:
            f.ret_1d[i] = close[i] / close[i - 1] - 1.0
            f.log_ret_1d[i] = math.log(close[i] / close[i - 1])

    f.sma_5 = _rolling_mean(close, 5)
    f.sma_20 = _rolling_mean(close, 20)
    f.sma_50 = _rolling_mean(close, 50)
    f.ema_12 = _ema(close, 12)
    f.ema_26 = _ema(close, 26)

    f.macd = [NaN] * n
    for i in range(n):
        if not math.isnan(f.ema_12[i]) and not math.isnan(f.ema_26[i]):
            f.macd[i] = f.ema_12[i] - f.ema_26[i]
    f.macd_signal = _ema(f.macd, 9)

    # RSI-14, Wilder's smoothing (not a naive SMA of gains/losses)
    f.rsi_14 = [NaN] * n
    window = 14
    avg_gain = 0.0
    avg_loss = 0.0
    for i in range(1, n):
        change = close[i] - close[i - 1]
        gain = change if change > 0 else 0.0
        loss = -change if change < 0 else 0.0
        if i <= window:
            avg_gain += gain / window
            avg_loss += loss / window
            if i == window:
                rs = math.inf if avg_loss == 0.0 else avg_gain / avg_loss
                f.rsi_14[i] = 100.0 - (100.0 / (1.0 + rs))
        else:
            avg_gain = (avg_gain * (window - 1) + gain) / window
            avg_loss = (avg_loss * (window - 1) + loss) / window
            rs = math.inf if avg_loss == 0.0 else avg_gain / avg_loss
            f.rsi_14[i] = 100.0 - (100.0 / (1.0 + rs))

    # Rolling volatility of log returns, annualized (sqrt(252))
    f.vol_20 = _rolling_std(f.log_ret_1d, 20)
    f.vol_20 = [v * math.sqrt(252.0) if not math.isnan(v) else v for v in f.vol_20]

    # Bollinger bands (20, 2 std) on raw price std
    raw_std_20 = _rolling_std(close, 20)
    f.bb_upper_20 = [NaN] * n
    f.bb_lower_20 = [NaN] * n
    for i in range(n):
        if not math.isnan(f.sma_20[i]) and not math.isnan(raw_std_20[i]):
            f.bb_upper_20[i] = f.sma_20[i] + 2 * raw_std_20[i]
            f.bb_lower_20[i] = f.sma_20[i] - 2 * raw_std_20[i]

    # ATR-14, Wilder smoothing on true range
    f.atr_14 = [NaN] * n
    tr = [NaN] * n
    for i in range(1, n):
        a = high[i] - low[i]
        b = abs(high[i] - close[i - 1])
        c = abs(low[i] - close[i - 1])
        tr[i] = max(a, b, c)
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

    # Momentum-10
    f.momentum_10 = [NaN] * n
    for i in range(10, n):
        if close[i - 10] > 0:
            f.momentum_10[i] = close[i] / close[i - 10] - 1.0

    # Volume z-score over 20d window
    vol_mean_20 = _rolling_mean(volume, 20)
    vol_std_20 = _rolling_std(volume, 20)
    f.volume_zscore_20 = [NaN] * n
    for i in range(n):
        if not math.isnan(vol_mean_20[i]) and not math.isnan(vol_std_20[i]) and vol_std_20[i] > 0:
            f.volume_zscore_20[i] = (volume[i] - vol_mean_20[i]) / vol_std_20[i]

    return f
