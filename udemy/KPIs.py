def CAGR(DF):
  "function to calculate the Cumulative Annual Growth Rate of a trading strategy"
  df = DF.copy()
  df["return"] = DF["Adj Close"].pct_change()
  df["cum_return"] = (1 + df["return"]).cumprod()
  n = len(df)/252
  CAGR = (df["cum_return"][-1])**(1/n) - 1
  return CAGR

def volatility(DF):
  "function to calculate annualized volatility of a trading strategy"
  df = DF.copy()

  return df

def sharpe(DF, rf):
  "function to calculate Sharpe Ratio of a trading strategy"
  df = DF.copy()

  return df

def sortino(DF, rf):
  "function to calculate Sortino Ratio of a trading strategy"
  df = DF.copy()

  return df

def max_dd(DF):
  "function to calculate max drawdown"
  df = DF.copy()

  return df

def calmar(DF):
  "function to calculate calmar ratio"
  df = DF.copy()
  
  return df