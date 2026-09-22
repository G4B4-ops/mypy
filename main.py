import yfinance as yf
tickers = [["AAPL"]]
prices = yf.download(tickers, start="2020-01-01", end="2021-01-01"  )
print(prices.head())
