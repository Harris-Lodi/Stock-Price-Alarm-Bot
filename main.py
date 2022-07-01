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

# get current working directory
cur_dir = os.getcwd()

upper_limits = [140, 163.1, 154.2, 77.6, 381]
lower_limits = [139.5, 163, 154.1, 77.4, 380.9]

# function to compare price:
def Check_Price():

    print("Stock check started!")

    # get the last close price before continuing
    last_prices = [web.DataReader(ticker, "yahoo")["Adj Close"][-1] for ticker in tickers]
    print(last_prices)

    for i in range(len(tickers)):

        if last_prices[i] > upper_limits[i]:
            notification = Notify()
            notification.title = "Upper Limit Breached!"
            notification.message = "Price of " + str(tickers[i]) + " is Too High, a good time to sell!"
            notification.audio = str(cur_dir) + "/Audio/Chime.wav"
            notification.icon = str(cur_dir) + "/Icons/candlestick.png"
            notification.send()
            print("Price of " + str(tickers[i]) + " is Too High, a good time to sell!")
            time.sleep(1)
        elif last_prices[i] < lower_limits[i]:
            notification = Notify()
            notification.title = "Lower Limit Breached!"
            notification.message = "Price of " + str(tickers[i]) + " is Too Low, a good time to buy!"
            notification.audio = str(cur_dir) + "/Audio/Chime.wav"
            notification.icon = str(cur_dir) + "/Icons/candlestick.png"
            notification.send()
            print("Price of " + str(tickers[i]) + " is Too Low, a good time to buy!")
            time.sleep(1)
        else:
            print("No Price border was hit this tick!")
            time.sleep(1)
            break
    
    print("Restarting loop in 45 seconds!")
    # delay for a number of seconds before continuing
    time.sleep(5)

    #Check_Price()
        
def updator():

    # running always while true
    while True:

        user_input = input("Enter 'Y' to start/Continue the program, or 'N' to exit: ")

        if user_input.upper().strip() == 'Y':
            Check_Price()
        elif user_input.upper().strip() == 'N':
            break
        else:
            print("Please enter a valid response, either yes 'Y' or no 'N'!")
            pass


updator()