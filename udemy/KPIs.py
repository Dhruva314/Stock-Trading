import numpy as np
import pandas as pd

def CAGR(DF):
  "function to calculate the Cumulative Annual Growth Rate of a trading strategy"
  df = DF.copy()
  # Here the strategy used is buying and holding long until the end of the DF
  df["return"] = DF["Close"].pct_change()
  df["cum_return"] = (1 + df["return"]).cumprod()
  n = len(df)/252
  CAGR = (df["cum_return"][-1])**(1/n) - 1
  return CAGR

def volatility(DF):
  "function to calculate annualized volatility of a trading strategy"
  "DF must be in daily closes"
  df = DF.copy()
  df["return"] = df["Close"].pct_change()
  vol = df["return"].std() * np.sqrt(252)
  return vol

def sharpe(DF, rf):
  "function to calculate Sharpe Ratio of a trading strategy"
  df = DF.copy()
  return (CAGR(df) - rf)/volatility(df)

def sortino(DF, rf):
  "function to calculate Sortino Ratio of a trading strategy"
  df = DF.copy()
  df["return"] = df["Close"].pct_change()
  # Removes positive returns
  neg_return = np.where(df["return"]>0,0,df["return"])
  # Calulates downward deviation approach where negative returns are penalised more
  neg_vol = np.sqrt((pd.Series(neg_return[neg_return != 0]) ** 2).mean() * 252)
  # Calculates the usual std of the regative returns
  #neg_vol = pd.Series(neg_return[neg_return != 0]).std() * np.sqrt(252)
  return (CAGR(df) - rf)/neg_vol

def max_dd(DF):
  "function to calculate max drawdown"
  df = DF.copy()
  df["return"] = df["Close"].pct_change()
  df["cum_return"] = (1+df["return"]).cumprod()
  df["cum_roll_max"] = df["cum_return"].cummax()
  df["drawdown"] = df["cum_roll_max"] - df["cum_return"]
  return (df["drawdown"]/df["cum_roll_max"]).max()

def calmar(DF):
  "function to calculate calmar ratio"
  df = DF.copy()
  return CAGR(df)/max_dd(df)