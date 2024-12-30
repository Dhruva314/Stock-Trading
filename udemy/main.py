import indicators as indi
import pandas as pd
import yfinance as yf
import csv

ohlcv_data =  {}
tickers = [
  "AAPL", 
  # "MSFT", 
  # "AMZN", 
  # "GOOGL", 
  # "GOOG", 
  # "NVDA", 
  # "TSLA",
  # "META"
]

# looping over tickers and storing OHLCV dataframe in dictionary
for ticker in tickers:
  temp = yf.download(ticker,period='1d',interval='15m')
  temp.dropna(how="any",inplace=True)
  ohlcv_data[ticker] = temp

for ticker in ohlcv_data:
  ohlcv_data[ticker][["MACD","SIGNAL"]] = indi.MACD(ohlcv_data[ticker])
  ohlcv_data[ticker]["RSI"] = indi.RSI(ohlcv_data[ticker])
  ohlcv_data[ticker]["ATR"] = indi.ATR(ohlcv_data[ticker])
  ohlcv_data[ticker]["ADX"] = indi.ADX(ohlcv_data[ticker],20)
  # ohlcv_data[ticker][["MB","UB","LB","BB_Width"]] = indi.BollBands(ohlcv_data[ticker])

print(ohlcv_data)
