import os
import time 
import pandas_datareader as web
from notifypy import Notify

# example on how to use notify
'''
notification = Notify()
notification.title = "Cool Title"
notification.message = "bottom text"
notification.audio = "path/to/audio/file.wav"
notification.icon = "path/to/icon/png"
notification.send()
'''

tickers = ["AAPL", "FB", "NVDA", "AMD", "SPY"]

# one time load of stock prices to see what they are
# using yahoo api, iloc is -1 for last time on api list, close price
'''
for ticker in tickers:
    print(web.DataReader(ticker, "yahoo").iloc[-1]['Close'])
'''

upper_limits = [200, 200, 200, 100, 400]
lower_limits = [100, 100, 100, 70, 350]

# function to compare price:
def Check_Price():

    # get the last close price before continuing
    last_prices = [web.DataReader(ticker, "yahoo")["Adj Close"][-1] for ticker in tickers]
    print(last_prices)

    # delay for a number of seconds before continuing
    time.sleep(45)

    for i in range(len(tickers)):

        if last_prices[i] > upper_limits[i]:
            notification = Notify()
            notification.title = "Upper Limit Breached!"
            notification.message = "Price of " + str(tickers[i]) + " is Too High, a good time to sell!"
            notification.audio = str(cur_dir) + "/Audio/Chime.wav"
            notification.icon = str(cur_dir) + "/Icons/candlestick.png"
            notification.send()
        elif last_prices[i] < lower_limits[i]:
            notification = Notify()
            notification.title = "Lower Limit Breached!"
            notification.message = "Price of " + str(tickers[i]) + " is Too Low, a good time to buy!"
            notification.audio = str(cur_dir) + "/Audio/Chime.wav"
            notification.icon = str(cur_dir) + "/Icons/candlestick.png"
            notification.send()
        else:
            pass
        # place another time.sleep to add a delay between the tickers
        time.sleep(5)

# running always while true
while True:

    '''
    user_input = input("Enter 'Y' to start/Continue the program, or 'N' to exit: ")

    if user_input == "Y":
        Check_Price()
    elif user_input == "N":
        break # breaks infinite while loop
    else:
        pass
    '''

    Check_Price()


    