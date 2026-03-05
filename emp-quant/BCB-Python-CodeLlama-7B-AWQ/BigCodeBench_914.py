import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
def task_func(df):
    # Create a new dataframe with the closing prices for the next 7 days
    new_df = pd.DataFrame(index=pd.date_range(df.index[-1], periods=7, freq='D'))
    new_df['Close'] = np.nan

    # Fill in the closing prices for the next 7 days using linear regression
    for i in range(7):
        X = df.index[:-i]
        y = df['Close'][:-i]
        model = LinearRegression().fit(X, y)
        new_df['Close'][i] = model.predict(new_df.index[i])

    # Plot the data
    ax = new_df['Close'].plot(kind='line', label='Predicted closing prices')
    ax.set_xlabel('Date')
    ax.set_ylabel('Closing price')
    ax.set_title('Predicted closing prices for the next 7 days')

    return new_df['Close'], ax
df = pd.read_csv('data.csv', index_col='Date', parse_dates=True)