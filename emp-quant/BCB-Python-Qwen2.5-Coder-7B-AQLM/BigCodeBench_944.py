
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(start_date='2016-01-01', periods=13, freq='WOM-2FRI', seed=0):
    np.random.seed(seed)
    dates = pd.date_range(start=start_date, periods=periods, freq=freq)
    prices = np.random.uniform(100, 500, size=periods)
    df = pd.DataFrame({'Date': dates, 'Price': prices})
    fig, ax = plt.subplots()
    ax.plot(df['Date'], df['Price'], marker='o')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.set_title('Share Price Series')
    return df, ax