# File with functions to calculate the value of common Technical Indicators (TI)

import pandas as pd
import numpy as np

def MACD(DF, f_period=12, s_period=26, ewm_span=9):
  """function to calculate MACD
      typical values for:
        period for fast movign avg = 12; 
        period for show movign avg = 26; 
        Exp weighted mean span =9"""
  df = DF.copy()
  df["ma_fast"] = df["Close"].ewm(span=f_period, min_periods=f_period).mean()
  df["ma_slow"] = df["Close"].ewm(span=s_period, min_periods=s_period).mean()
  df["macd"] = df["ma_fast"] - df["ma_slow"]
  df["signal"] = df["macd"].ewm(span=ewm_span, min_periods=ewm_span).mean()
  return df.loc[:,["macd","signal"]]

def ATR(DF, ewm_span=14):
  "function to calculate True Range and Average True Range"
  df = DF.copy()
  df["H-L"] = df["High"] - df["Low"]
  df["H-PC"] = abs(df["High"] - df["Close"].shift(1))
  df["L-PC"] = abs(df["Low"] - df["Close"].shift(1))
  df["TR"] = df[["H-L","H-PC","L-PC"]].max(axis=1, skipna=False)
  df["ATR"] = df["TR"].ewm(com=ewm_span, min_periods=ewm_span).mean()
  return df["ATR"]

def BollBands(DF, window=14):
  "function to calculate Bollinger Band"
  df = DF.copy()
  df["MB"] = df["Close"].rolling(window).mean()
  df["UB"] = df["MB"] + 2*df["Close"].rolling(window).std(ddof=0)
  df["LB"] = df["MB"] - 2*df["Close"].rolling(window).std(ddof=0)
  df["BB_Width"] = df["UB"] - df["LB"]
  return df[["MB","UB","LB","BB_Width"]]

def RSI(DF, n=14):
  "function to calculate RSI"
  df = DF.copy()
  df["change"] = df["Adj Close"] - df["Adj Close"].shift(1)
  df["gain"] = np.where(df["change"]>=0, df["change"], 0)
  df["loss"] = np.where(df["change"]<0, -1*df["change"], 0)
  df["avgGain"] = df["gain"].ewm(alpha=1/n, min_periods=n).mean()
  df["avgLoss"] = df["loss"].ewm(alpha=1/n, min_periods=n).mean()
  df["rs"] = df["avgGain"]/df["avgLoss"]
  df["rsi"] = 100 - (100/ (1 + df["rs"]))
  return df["rsi"]


def ADX(DF, n=20):
  "function to calculate ADX"
  df = DF.copy()
  df["ATR"] = ATR(DF, n)
  df["upmove"] = df["High"] - df["High"].shift(1)
  df["downmove"] = df["Low"].shift(1) - df["Low"]
  df["+dm"] = np.where((df["upmove"]>df["downmove"]) & (df["upmove"] >0), df["upmove"], 0)
  df["-dm"] = np.where((df["downmove"]>df["upmove"]) & (df["downmove"] >0), df["downmove"], 0)
  df["+di"] = 100 * (df["+dm"]/df["ATR"]).ewm(alpha=1/n, min_periods=n).mean()
  df["-di"] = 100 * (df["-dm"]/df["ATR"]).ewm(alpha=1/n, min_periods=n).mean()
  df["ADX"] = 100* abs((df["+di"] - df["-di"])/(df["+di"] + df["-di"])).ewm(alpha=1/n, min_periods=n).mean()
  return df["ADX"]

def Renko(DF, hourly_df):
  df = DF.copy()
  return df

