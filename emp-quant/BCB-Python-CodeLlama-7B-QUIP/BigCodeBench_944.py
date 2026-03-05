
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(start_date='2016-01-01', periods=13, freq='WOM-2FRI', seed=0):
    np.random.seed(seed)
    dates = pd.date_range(start_date, periods=periods, freq=freq)
    prices = np.random.randint(100, 500, size=periods)
    df = pd.DataFrame({'Date': dates, 'Price': prices})
    fig, ax = plt.subplots()
    ax.plot(df['Date'], df['Price'])
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.set_title('Share Prices')
    return df, fig