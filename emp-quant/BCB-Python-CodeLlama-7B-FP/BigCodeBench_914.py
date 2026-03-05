import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
def task_func(df):
    # Create a new DataFrame with the closing prices for the next 7 days
    future_prices = pd.DataFrame(index=pd.date_range(df.index[-1], periods=7, freq='D'))
    future_prices['Close'] = np.nan

    # Fill in the closing prices for the next 7 days using simple linear regression
    lr = LinearRegression()
    lr.fit(df['Close'].values.reshape(-1, 1), df.index.values.reshape(-1, 1))
    future_prices['Close'] = lr.predict(future_prices.index.values.reshape(-1, 1))

    # Plot the data
    fig, ax = plt.subplots()
    ax.plot(df['Close'], label='Actual')
    ax.plot(future_prices['Close'], label='Predicted')
    ax.set_xlabel('Date')
    ax.set_ylabel('Closing Price')
    ax.legend()
    return (future_prices['Close'].tolist(), ax)
df = pd.read_csv('data.csv', index_col='Date', parse_dates=['Date'])