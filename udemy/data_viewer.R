library(readr)

while (TRUE) {
  ticker_data <- read_csv("//wsl.localhost/Ubuntu/home/dhruva/ticker_data.csv")
  View(ticker_data)
  Sys.sleep(60)   # Wait for 1 minute before refreshing
}


# Code for Console
# library(readr)
# View(read_csv("//wsl.localhost/Ubuntu/home/dhruva/ticker_data.csv"))

