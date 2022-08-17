import pandas as pd 
from alpha_vantage.timeseries import TimeSeries
import time 

# This is now useless since alpha-vantage and most free APIs do not have real time intraday data avaialble now

api_key = ''

ts = TimeSeries(key = api_key, output_format = 'pandas')
# data, meta_Data = ts.get_intraday(symbol = 'AMD', interval = '1min', outputsize = 'full')
# print(data)
'''
# while loop to get the data every minute
while True:

    # get data and save to excel file 
    data, meta_Data = ts.get_intraday(symbol = 'AMD', interval = '1min', outputsize = 'full')
    data.to_excel("output.xlsx")
    time.sleep(60)
'''