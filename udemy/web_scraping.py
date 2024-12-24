import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.google.com/finance/quote/AAPL:NASDAQ'
page = requests.get(url)
page_content = page.content
# print(page_content)


# Send a GET request to the URL
response = requests.get(url)
response.raise_for_status()  # Raise an HTTPError for bad responses

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Locate the section containing the summary (specific tag/classes might need adjustment)
data_parsed = soup.find_all('div', {'class': 'P6K39c'})  # Example class for illustration; may need adjustment
labels_parsed = soup.find_all('div', {'class': 'mfs7Fc'})

labels = []
for index, text in enumerate(labels_parsed):
  # print(index)
  # print(text.get_text(strip = True))
  labels.append(text.get_text(strip = True))

data = []
for index, text in enumerate(data_parsed):
  # print(index)
  # print(text.get_text(strip = True))
  data.append(text.get_text(strip = True))

df = pd.DataFrame(data, index = labels)

print(df)

# data = {}

# if summary:
#   text = (summary.get_text(separator = '####'))
#   start_index = text.find('Previous close')
#   end_index = text.find('')
#   data = text[start_index:]
#   data = text.split('####')


#   # # Loop through the child elements of the summary
#   # for i, child in enumerate(summary.find_all(recursive=False)):  # Use recursive=False to avoid nested children
#   #     text = child.get_text(strip=True)
#   #     data[f'segment_{i + 1}'] = text  # Store each text segment in the dictionary

#   # # Print the stored data
#   # for key, value in data.items():
#   #     print(f"{key}: {value}")
# else:
#   print("Summary section not found. The page may use dynamic JavaScript rendering.")
# # # Print path data
# # for row in summary_table:
# #     data = row.find_all('div', {'class': 'gyFHrc'})
# #     for entry in data:
# #       print(entry.get_text)


