import os
import time 
import pandas_datareader as web
import pandas as pd
import datetime
from IPython.display import display

df = pd.DataFrame(columns=['Date', 'Time', 'Price', 'Volume', 'RSI'])
# df = df.set_index(pd.DatetimeIndex(df['Time'].values))

def get_data():

    # display(df)

    currenttime = datetime.datetime.now()

    current_date = str(currenttime.year) + '/' + str(currenttime.month) + '/' + str(currenttime.day)
    current_time = str(currenttime.hour) + ':' + str(currenttime.minute) + ':' + str(currenttime.second)

    price = web.DataReader('AMD', "yahoo").iloc[-1]['Close']
    volume = web.DataReader('AMD', "yahoo").iloc[-1]['Volume']

    df.loc[len(df.index)] = [current_date, current_time, price, volume, 0]

    # print('The date is: ' + current_date + ', The time is: ' + current_time + ', The price is: ' + str(price) + ', The volume is: ' + str(volume))

    # display(df)

def calc_RSI():

    delta = df['Price'].diff(1)

    delta = delta.dropna()

    # get the positive gains (up), and the negative losses (down)
    up = delta.copy()
    down = delta.copy()

    # keep only positive values for up(set any negative values to 0)
    up[up<0] = 0

    # keep only negative values for down(any positive values set to 0)
    down[down>0] = 0

    # Get the time period
    period = 14
    # calculate the average gain and the average loss
    avg_Gain = up.rolling(window=period).mean()
    avg_Loss = abs(down.rolling(window=period).mean())

    # calculate the RSI

    # calculate the Relative Strength(RS)
    RS = avg_Gain / avg_Loss

    # Calc the RSI
    RSI = 100.0 - (100.0 / (1.0 + RS))

    # create a new dataframe
    # new_df = pd.DataFrame()
    # new_df['Adj Close Price'] = df['Price']
    df['RSI'] = RSI

def store_data():

    get_data()
    calc_RSI()

    # df.loc[len(df.index)] = [get_data().current_date, get_data().current_time, get_data().price, get_data().volume, calc_RSI().RSI]

    display(df)

while True:

    store_data()

    time.sleep(60)