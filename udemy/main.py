import indicators as indi
import pandas as pd
import yfinance as yf

ohlcv_data =  {}
tickers = [
  "AAPL", 
  "MSFT", 
  "AMZN", 
  "GOOGL", 
  "GOOG", 
  "NVDA", 
  "TSLA",
  "META"
]

# looping over tickers and storing OHLCV dataframe in dictionary
for ticker in tickers:
  temp = yf.download(ticker,period='1mo',interval='15m')
  temp.dropna(how="any",inplace=True)
  ohlcv_data[ticker] = temp

ohlcv_data.to_csv('ohlcv_data')

for ticker in ohlcv_data:
  ohlcv_data[ticker][["MACD","SIGNAL"]] = indi.MACD(ohlcv_data[ticker])

