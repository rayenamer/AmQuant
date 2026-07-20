from amquant.loader import (
    load_market_data,
    describe,
    list_features,
    feature_summary,
    RAW_SERIES,
    FEATURE_SETS
)

# Usage:
load_market_data(verbose=True)

print(describe("macd_hist"))
print(describe("bb_percent_b"))
print(describe("vol_20"))

list_features()          # returns list of all features
feature_summary()        # prints nice overview