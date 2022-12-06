import yfinance as yf
import pandas as pd
import numpy
import math

ticker = yf.Ticker("AAPL")      # Stock Ticker "AAPL"

# History of ticker stock
# data = ticker.history(interval = '1d', start = '2022-12-01', end = '2022-12-03')
# data_1y = ticker.history(interval = '1d', period = '1y')

data_1y = ticker.history(interval = '1d', start = '2022-01-03')
data_1y_volume = data_1y["Volume"]

# Average Volume could be calculated
avg_volume = []
for i in range(0, len(data_1y_volume)) :
    if i < 2 :
        i += 1
    else:
        avg_volume.append(int((data_1y_volume[i] + data_1y_volume[i-1] + data_1y_volume[i-2])/3))

# Get Data Daily Volume
data_daily_volume = ticker.history(interval = '1d', start = '2022-01-05')
data_daily_volume = data_daily_volume["Volume"]

# Get Index = Volume / Average3daysVolume
Index = []
for i in range(0, len(data_daily_volume)):
    Index.append(round(data_daily_volume[i]/avg_volume[i],2))

print(Index)


# Print two volume data
# print(avg_volume)
# print("###########################")
# print(data_daily_volume)
