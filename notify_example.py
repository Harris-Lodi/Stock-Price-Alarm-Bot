from notifypy import Notify
import os

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
    # notification.audio = str(cur_dir) + "/Audio/stomping-rock-four-shots.wav"
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