import yfinance as yf
import pandas as pd
import datetime as dt
import time

from alpha_vantage.timeseries import TimeSeries

start_date = dt.date.today() - dt.timedelta(days = 365)
end_date = dt.date.today
close_price = pd.DataFrame()
ticker_data = {}
tickers = [
  "AAPL", 
  "MSFT", 
  "AMZN", 
  "GOOGL", 
  "GOOG", 
  "NVDA", 
  "TSLA"
]

# # To make an array of close prices using yfinance
# for ticker in tickers:
#   close_price[f'{ticker}'] = yf.download(
#     tickers = ticker,
#     period = '6mo',
#     interval= '1mo'
#   )["Close"]

# close_price.to_csv('close_price_data.csv')


# # To make an array of all the data available from yfinance
# for ticker in tickers:
#   ticker_data[ticker] = yf.download(tickers = ticker, period = '6mo', interval= '1mo')
# print(ticker_data)

# # To make an array of all the close prices from alpha_vantage (backup)
# api_call_count = 0
# start_time = time.time()
# for ticker in tickers:
#   # if (api_call_count < 5):
#     ts = TimeSeries(key='2TPZETZ4XAK9K3D9', output_format = 'pandas')
#     data = ts.get_daily(symbol = ticker, outputsize = 'full')[0]
#     # renames colums to be more clean
#     data.columns = ['open', 'high', 'low', 'close', 'volume']
#     #stores only close into close_price array
#     close_price[ticker] = data['close']
#     api_call_count += 1
#     end_time = time.time()
  
#   # # Accounts for limit of 5 calls a minute
#   # elif ((end_time - start_time) <= 60):
#   #   print('Reached 5 call a minute max')
#   #   time.sleep(60 - (end_time - start_time))
#   #   start_time = time.time()

# close_price.to_csv('close_price_data.csv')
