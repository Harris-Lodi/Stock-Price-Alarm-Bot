import pandas as pd
import numpy as np
from IPython.display import display
import time 
import matplotlib.pyplot as plt
import datetime as dt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
import threading

df = pd.DataFrame(columns=['x', 'y'])
fig = plt.figure()
plt.style.use('fivethirtyeight')

def add_data():

    x = np.random.randint(0,100)
    y = np.random.randint(0,100)

    df.loc[len(df.index)] = [x, y]

def animate(i):

    

    x = df.index
    y = df['x']
    z = df['y']

    plt.cla()

    plt.plot(x, y, z)

    plt.title('Test animated graph over index values')
    plt.ylabel('Values')
    plt.xticks(rotation=45, ha='right')

    # plt.show()
   
def plot_animate():
    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.show()

def calculate_df():

    while True:
        add_data()
        display(df)
        time.sleep(3)


x = threading.Thread(target=calculate_df, args=())
# y = threading.Thread(target=plot_animate(), args=())



x.start()
# y.start()
plot_animate()
x.join()
# y.join()

# This technically works now, but is a really ugly setup!