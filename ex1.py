import yfinance as yf
import pandas as pd
import numpy
import math
import matplotlib.pyplot as plt
import datetime
from datetime import date, timedelta



# History of ticker stock
# data = ticker.history(interval = '1d', start = '2022-12-01', end = '2022-12-03')
# data_1y = ticker.history(interval = '1d', period = '1y')

ticker = yf.Ticker("ABNB")      # Stock Ticker "AAPL"
data_1y = ticker.history(interval = '1d', start = '2022-01-03')
data_1y_volume = data_1y["Volume"]

# Average Volume calculated
avg_volume = []
for i in range(0, len(data_1y_volume)) :
    if i < 4 :
        i += 1
    else:
        avg_volume.append(int((data_1y_volume[i] + data_1y_volume[i-1] + data_1y_volume[i-2]+data_1y_volume[i-3]+data_1y_volume[i-4])/5))

# Get Data Daily Volume
data_daily = ticker.history(interval = '1d', start = '2022-01-07')
data_daily_volume = data_daily["Volume"]

# Get Index = Volume / Average5daysVolume
Index = []
for i in range(0, len(data_daily_volume)-1):
    Index.append(round((data_daily_volume[i]-avg_volume[i])/avg_volume[i]*100,2))

# Get daily up down
data_daily_updown = ticker.history(interval = '1d', start = '2022-01-08')
data_1y_updown = round((data_daily_updown["Close"] - data_daily_updown["Open"])/(data_daily_updown["Open"]) * 100, 2)




########################################################################################################
##   There is no correlation between the daily high(close) price and the volume of one day before    ####
##   So.. Try "price after first hour" & volume                                                      ####
######################################################################################################## 


data_hour = ticker.history(interval  = '1h', start = '2022-01-08')

data_hourly_updown = []
for i in range(0, len(data_daily_updown)):
    t_find = data_daily_updown.index[i]
    t_find_str = t_find.strftime("%Y-%m-%d")
    data_hourly_updown.append(round((data_hour[t_find_str]['Close'][0] - data_hour[t_find_str]['Open'][0])/(data_hour[t_find_str]['Open'][0]) * 100, 2))


plt.plot(Index, data_hourly_updown,'ro')
plt.axis([min(Index), max(Index), min(data_hourly_updown), max(data_hourly_updown)])
plt.show()