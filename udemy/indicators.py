# File with functions to calculate the value of common Technical Indicators (TI)

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
  df = DF.copy()
  return df

def BollBands(DF, ewm_span=14):
  df = DF.copy()
  return df

def RSI(DF, ewm_span=14):
  df = DF.copy()
  return df

def ADX(DF, ewm_span=20):
  df = DF.copy()
  return df

def Renko(DF, hourly_df):
  df = DF.copy()
  return df

