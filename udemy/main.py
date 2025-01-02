import indicators as indi
import KPIs as kpi
import pandas as pd
import yfinance as yf
import os

ohlcv_data =  {}
hour_data = {}
renko_data = {}

risk_free_rate = 0.03

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
  temp = yf.download(ticker,period='1d',interval='15m')
  temp.dropna(how="any",inplace=True)
  ohlcv_data[ticker] = temp

  temp = yf.download(ticker,period='1y',interval='1h')
  temp.dropna(how="any",inplace=True)
  hour_data[ticker] = temp

for ticker in ohlcv_data:
  # Calculates MACD
  ohlcv_data[ticker][["MACD","SIGNAL"]] = indi.MACD(ohlcv_data[ticker])
  # Calculates RSI
  ohlcv_data[ticker]["RSI"] = indi.RSI(ohlcv_data[ticker])
  # Calculates ATR
  ohlcv_data[ticker]["ATR"] = indi.ATR(ohlcv_data[ticker])
  # Calculates ADX
  ohlcv_data[ticker]["ADX"] = indi.ADX(ohlcv_data[ticker],20)
  # Calculates Bollinger Bands and merces results into the DataFrame
  bb_data = indi.BollBands(ohlcv_data[ticker])
  ohlcv_data[ticker][["MB","UB","LB","BB_Width"]] = indi.BollBands(ohlcv_data[ticker])
  # Formats the data to fit Renko
  renko_data[ticker] = indi.Renko_DF(ohlcv_data[ticker],hour_data[ticker], ticker)

  # KPI Results
  print("CAGR of {} = {}".format(ticker,kpi.CAGR(ohlcv_data[ticker])))
  print("vol for {} = {}".format(ticker,kpi.volatility(ohlcv_data[ticker])))
  print("Sharpe of {} = {}".format(ticker,kpi.sharpe(ohlcv_data[ticker],risk_free_rate)))
  print("Sortino of {} = {}".format(ticker,kpi.sortino(ohlcv_data[ticker],risk_free_rate)))
  print("max drawdown of {} = {}".format(ticker,kpi.max_dd(ohlcv_data[ticker])))
  print("calmar ratio of {} = {}".format(ticker,kpi.calmar(ohlcv_data[ticker])))

# print(ohlcv_data["AAPL"]["Close"].pct_change())

path = "/home/dhruva/Stock-Trading/udemy/exports"
for ticker, df in ohlcv_data.items():
  file_path = os.path.join(path, f"{ticker}.csv")
  df.to_csv(file_path, index=False)

for ticker, df in renko_data.items():
  file_path = os.path.join(path+"/renko", f"{ticker}_renko.csv")
  df.to_csv(file_path, index=False)

  