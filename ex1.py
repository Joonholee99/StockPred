import yfinance as yf

ticker = yf.Ticker("AAPL")

data = ticker.history(interval = '1h', start = '2022-12-01')

print(data)


#print(data.info["volume"])

#print(data.info["averageVolume"])
#print(data.info["averageVolume10days"])
