"""Universe loader. Mirrors include/qde/universe.hpp + src/universe.cpp."""
from __future__ import annotations
import csv
from dataclasses import dataclass


@dataclass
class Instrument:
    symbol: str = ""
    name: str = ""
    country: str = ""
    exchange: str = ""
    source: str = ""   # "yahoo" or "manual_csv"

    yahoo_symbol: str = ""
