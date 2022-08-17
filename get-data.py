import os
import time 
import pandas_datareader as web
import pandas as pd
import datetime
from IPython.display import display

df = pd.DataFrame(columns=['Date', 'Time', 'Price', 'Volume'])

while True:

    # display(df)

    currenttime = datetime.datetime.now()

    current_date = str(currenttime.year) + '/' + str(currenttime.month) + '/' + str(currenttime.day)
    current_time = str(currenttime.hour) + ':' + str(currenttime.minute) + ':' + str(currenttime.second)

    price = web.DataReader('AMD', "yahoo").iloc[-1]['Close']
    volume = web.DataReader('AMD', "yahoo").iloc[-1]['Volume']

    df.loc[len(df.index)] = [current_date, current_time, price, volume]

    # print('The date is: ' + current_date + ', The time is: ' + current_time + ', The price is: ' + str(price) + ', The volume is: ' + str(volume))

    display(df)

    time.sleep(60)