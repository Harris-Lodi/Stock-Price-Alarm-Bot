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

notification = Notify()
notification.title = "Stock Price Alarm"

tickers = ["AAPL", "FB", "NVDA", "AMD", "SPY"]

# one time load of stock prices to see what they are
# using yahoo api, iloc is -1 for last time on api list, close price
'''
for ticker in tickers:
    print(web.DataReader(ticker, "yahoo").iloc[-1]['Close'])
'''

upper_limits = [200, 200, 200, 100, 400]
lower_limits = [100, 100, 100, 70, 350]

# running always while true
while True:

    # All of the following needs to be placed in a function 
    # though as it is, it wil repeat after the time.sleep line, a function makes this neater

    # get the last close price before continuing
    last_prices = [web.DataReader(ticker, "yahoo")["Adj Close"][-1] for ticker in tickers]
    print(last_prices)

    # delay for a number of seconds before continuing
    time.sleep(3)

    for i in range(len(tickers)):

        if last_prices[i] > upper_limits[i]:
            n_body = "Price for " + str(tickers[i]) + " is above the upper limit!"
            notification.message(self, n_body)
            notification.show()
        elif last_prices[i] < lower_limits[i]:
            pass
        # place another time.sleep to add a delay between the tickers
        time.sleep(1)
    