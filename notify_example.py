from notifypy import Notify
import os
import time

# get current working directory
cur_dir = os.getcwd()
# print(cur_dir)

'''
notification = Notify()
notification.title = "Cool Title"
notification.message = "bottom text"
notification.audio = str(cur_dir) + "/Audio/stomping-rock-four-shots.wav"
notification.icon = str(cur_dir) + "/Icons/candlestick.png"
notification.send()
'''

def notification_1():
    notification = Notify()
    notification.title = "Function Numba One!"
    notification.message = "First function"
    notification.audio = str(cur_dir) + "/Audio/Chime.wav"
    notification.icon = str(cur_dir) + "/Icons/candlestick.png"
    notification.send()

def notification_2():
    notification = Notify()
    notification.title = "Function Numba Two!"
    notification.message = "Second function"
    # notification.audio = str(cur_dir) + "/Audio/stomping-rock-four-shots.wav"
    notification.icon = str(cur_dir) + "/Icons/candlestick.png"
    notification.send()

def notification_3():
    notification = Notify()
    notification.title = "Function Numba Three!"
    notification.message = "Third function"
    # notification.audio = str(cur_dir) + "/Audio/stomping-rock-four-shots.wav"
    notification.icon = str(cur_dir) + "/Icons/candlestick.png"
    notification.send()

while True:
    user_input = input("Enter the function you want to run, choose 1, 2, or 3: ")

    if user_input == "1":
        notification_1()
        time.sleep(10)
    elif user_input == "2":
        notification_2()
        time.sleep(5)
    elif user_input == "3":
        notification_3()
        time.sleep(1)
    else:
        break # breaks infinite while loop