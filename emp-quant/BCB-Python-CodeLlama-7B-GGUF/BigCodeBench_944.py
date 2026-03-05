
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(start_date='2016-01-01', periods=13, freq='WOM-2FRI', seed=0):
    np.random.seed(seed)
    share_prices = np.random.uniform(100, 500, size=periods)
    share_prices = pd.Series(share_prices, index=pd.date_range(start_date, periods=periods, freq=freq))
    fig, ax = plt.subplots()
    ax.plot(share_prices.index, share_prices.values)
    ax.set_xlabel('Date')
    ax.set_ylabel('Share Price')
    ax.set_title('Share Price Series')
    return share_prices, fig