import yfinance as yf

data = yf.download("SPY", start="2000-01-01", end="2019-10-04" )

data.to_csv("SPY.csv")