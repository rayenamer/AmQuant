from amquant.dataSources.yahoo_finance import YahooFinanceClient

client = YahooFinanceClient()
series = client.download("MC.PA", "2024-01-01", "2024-06-01")
print(series.symbol, len(series.bars), series.bars[0].close if series.bars else None)