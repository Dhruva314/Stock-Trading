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

def RSI(DF, ewm_span=14):
  df = DF.copy()
  return df

def ADX(DF, ewm_span=20):
  df = DF.copy()
  return df

def Renko(DF, hourly_df):
  df = DF.copy()
  return df

