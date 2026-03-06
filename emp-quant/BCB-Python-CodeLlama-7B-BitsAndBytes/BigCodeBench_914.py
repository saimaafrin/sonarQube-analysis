
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def task_func(df):
    # Create a new dataframe with the predicted prices for the next 7 days
    predicted_prices = []
    for i in range(7):
        # Generate a new timestamp for the next day
        timestamp = df.index[-1] + pd.Timedelta(days=1)
        # Use the linear regression model to predict the price for the next day
        predicted_price = LinearRegression().fit(df.index, df.values).predict(timestamp)
        predicted_prices.append(predicted_price)

    # Create a new dataframe with the predicted prices and the actual prices
    predicted_prices_df = pd.DataFrame({'Predicted Price': predicted_prices, 'Actual Price': df.values[-7:]})

    # Plot the data
    fig, ax = plt.subplots()
    ax.plot(df.index, df.values, label='Actual Price')
    ax.plot(predicted_prices_df.index, predicted_prices_df['Predicted Price'], label='Predicted Price')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend()
    return (predicted_prices, ax)