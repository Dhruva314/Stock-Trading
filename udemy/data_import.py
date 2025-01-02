import yfinance as yf
import pandas as pd
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
import os
import pickle

# import time
# from alpha_vantage.timeseries import TimeSeries
year_period = 5
end_date = dt.date.today()
ohlcv_data =  {}
hour_data = {}

start_date = end_date - dt.timedelta(days = 365*year_period)
close_price = pd.DataFrame()
ticker_data = {}
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

folder_path = "/home/dhruva/Stock-Trading/udemy/imports/"

# Loop through all files in the folder and delete them before importing new data
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        os.remove(file_path)

# looping over tickers and storing OHLCV dataframe in dictionary
for ticker in tickers:
  # saving ohlcv_data dict
  temp = yf.download(ticker,period='1d',interval='15m')
  temp.dropna(how="any",inplace=True)
  ohlcv_data[ticker] = temp

  with open(folder_path+"ohlcv_data.pkl", "wb") as file:
    pickle.dump(ohlcv_data, file)

  # saving hour_data dict
  temp = yf.download(ticker,period='1y',interval='1h')
  temp.dropna(how="any",inplace=True)
  hour_data[ticker] = temp
  
  with open(folder_path+"hour_data.pkl", "wb") as file:
    pickle.dump(hour_data, file)

# # Charting data using log returns
# 
# # To make an array of close prices using yfinance
# for ticker in tickers:
#   close_price[f'{ticker}'] = yf.download(
#     tickers = ticker,
#     start = start_date,
#     end = end_date,
#     interval='3mo'
#   )["Close"]

# close_price.fillna(value=0, inplace=True)
# log_change = np.log(close_price / close_price.shift(1))

# # Iterate over each row and column using `iterrows()`
# for index, row in log_change.iterrows():
#   for ticker in tickers:
#     if np.isinf(row[ticker]):  # Check if the value is 'inf'
#       log_change.at[index, ticker] = None  # Set the value to None

# log_change.plot()
# plt.savefig('plot.png')

# log_change.to_csv('log_change.csv')
# close_price.to_csv('close_price_data.csv')

