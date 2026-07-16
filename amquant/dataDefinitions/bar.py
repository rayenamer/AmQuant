"""Shared data model. Mirrors include/qde/bar.hpp.

Everything downstream (csv_io, features) depends only on this module,
same as in the C++ version -- it's the one type both Yahoo-sourced and
manually-loaded (BVMT) data get normalized into.
"""
from dataclasses import dataclass, field


@dataclass
class Bar:
    """One trading day (or bar) of market data for a single instrument."""
    timestamp_utc: int = 0   # unix seconds
    open: float = 0.0
    high: float = 0.0
    low: float = 0.0
    close: float = 0.0
    adj_close: float = 0.0   # dividend/split adjusted; falls back to close if unknown
    volume: float = 0.0


@dataclass
class Series:
    """Raw series for one instrument."""
    symbol: str = ""
    exchange: str = ""   # e.g. "BVMT", "EURONEXT_PARIS", "XETRA"
    country: str = ""    # e.g. "TN", "FR", "DE"
    bars: list = field(default_factory=list)   # list[Bar], ascending by timestamp
