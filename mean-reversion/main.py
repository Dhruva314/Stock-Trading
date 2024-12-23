import yfinance as yf
import pandas as pd
import datetime as dt

start_date = dt.date.today() - dt.timedelta(days = 365)
end_date = dt.date.today
close_price = pd.DataFrame()
tickers = [
  "AAPL", 
  "MSFT", 
  "AMZN", 
  "GOOGL", 
  "GOOG", 
  "NVDA", 
  "TSLA"
]

ticker_data = {}

for ticker in tickers:
  close_price[ticker] = yf.download(tickers = ticker, period = '6mo', interval= '1mo')['Adj Close']
  
for ticker in tickers:
  ticker_data[ticker] = yf.download(tickers = ticker, period = '6mo', interval= '1mo')
  

close_price.to_csv('close_price_data.csv')
ticker_data.to_csv('ticker_data.csv')