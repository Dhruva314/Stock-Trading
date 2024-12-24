import requests
from bs4 import BeautifulSoup
import pandas as pd

nasdaq_tickers = [
  "AAPL", 
  "MSFT", 
  "AMZN", 
  "GOOGL", 
  "GOOG", 
  "NVDA", 
  "TSLA"
]

for ticker in nasdaq_tickers:
  url = f"https://www.google.com/finance/quote/{ticker}:NASDAQ"
  page = requests.get(url)

  # Parse the HTML content of the page
  soup = BeautifulSoup(page.text, 'html.parser')

  # Locates the Description and Data
  data_parsed = soup.find_all('div', {'class': 'P6K39c'}) 
  labels_parsed = soup.find_all('div', {'class': 'mfs7Fc'})

  labels = []
  for index, text in enumerate(labels_parsed):
    labels.append(text.get_text(strip = True))

  data = []
  for index, text in enumerate(data_parsed):
    data.append(text.get_text(strip = True))

  # Stores the data into a pandas Dataframe
  df = pd.DataFrame(data, index = labels)

  print('__________________________________________________________')
  print(ticker)
  print(df)

