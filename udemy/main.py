import indicators as indi
import KPIs as kpi
import os
import pickle

ohlcv_data =  {}
hour_data = {}
renko_data = {}
tickers = []

risk_free_rate = 0.03

folder_path = "/home/dhruva/Stock-Trading/udemy/"

# Loop through all files in the folder and delete them
# to remove old/redundant exports
for filename in os.listdir(folder_path+"exports"):
  file_path = folder_path+"exports/"+filename
  if os.path.isdir(file_path):
    for filename2 in os.listdir(file_path):
      os.remove(os.path.join(file_path, filename2))
  else:
    os.remove(file_path)
    tickers.append(file_path)

with open(folder_path+"imports/ohlcv_data.pkl", "rb") as file:
  ohlcv_data = pickle.load(file)

with open(folder_path+"imports/hour_data.pkl", "rb") as file:
  hour_data = pickle.load(file)

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
  print('--------------------------------------------------------------------')
  print(ticker)
  print('-----------')
  print("CAGR of {} = {}".format(ticker,kpi.CAGR(ohlcv_data[ticker])))
  print("vol for {} = {}".format(ticker,kpi.volatility(ohlcv_data[ticker])))
  print("Sharpe of {} = {}".format(ticker,kpi.sharpe(ohlcv_data[ticker],risk_free_rate)))
  print("Sortino of {} = {}".format(ticker,kpi.sortino(ohlcv_data[ticker],risk_free_rate)))
  print("max drawdown of {} = {}".format(ticker,kpi.max_dd(ohlcv_data[ticker])))
  print("calmar ratio of {} = {}".format(ticker,kpi.calmar(ohlcv_data[ticker])))

path = folder_path+ "exports"
for ticker, df in ohlcv_data.items():
  file_path = os.path.join(path, f"{ticker}.csv")
  df.to_csv(file_path, index=False)

for ticker, df in renko_data.items():
  file_path = os.path.join(path+"/renko", f"{ticker}_renko.csv")
  df.to_csv(file_path, index=False)

  