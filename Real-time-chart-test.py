import pandas as pd
import numpy as np
from IPython.display import display
import time 
import matplotlib.pyplot as plt
import datetime as dt
from matplotlib.animation import FuncAnimation

df = pd.DataFrame(columns=['x', 'y'])
plt.style.use('fivethirtyeight')

def add_data():

    x = np.random.randint(0,100)
    y = np.random.randint(0,100)

    df.loc[len(df.index)] = [x, y]

def animate():

    x = df['x']
    y = df['y']

    plt.cla()

    plt.plot(x, y)
    plt.show()
   

while True:

    add_data()
    display(df)
    animate()
    
    time.sleep(3)

# to add to data frame and then to plot it out will require multi-threading, or another process to handle the graphing,
# also can help saving the dataframe data in a csv before plotting it, need to work on this later