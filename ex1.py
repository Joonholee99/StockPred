import yfinance as yf
import pandas as pd
import numpy

ticker = yf.Ticker("AAPL")      # Stock Ticker "AAPL"

# History of ticker stock
# data = ticker.history(interval = '1d', start = '2022-12-01', end = '2022-12-03')
# print(type(data.index))
data_1y = ticker.history(interval = '1d', period = '1y')

data_volume = data_1y["Volume"]
# print(data_volume[0])

# Average Volume could be calculated
i = 0
avg_volume = []
for i in range(0, len(data_volume)) :
    if i < 2 :
        i += 1
    else:
        avg_volume.append((data_volume[i] + data_volume[i-1] + data_volume[i-2])/3)

print(avg_volume)
print("###########################")
print(data_volume)