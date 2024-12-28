from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


path = '/home/dhruva/Stock-Trading/udemy/chromedriver-linux64/chromedriver-linux64/chromedriver'

service = Service(path)
service.start()

tickers = [
  'AAPL'
]

ticker = tickers[0]

url = f"https://finance.yahoo.com/quote/{ticker}/financials/"

driver = webdriver.Chrome(service=service)
driver.get(url)


# Wait for the element to be visible
wait = WebDriverWait(driver, 10)
table = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="nimbus-app"]/section/section/section/article/article/section/div')))
print(table.text)

print(12345678901234567890123456789012345678901234567890)

driver.quit()