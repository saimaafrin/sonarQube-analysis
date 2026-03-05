import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
def task_func(df):
    # Ensure the dataframe has a datetime index
    df.index = pd.to_datetime(df.index)
    
    # Extract the closing prices
    prices = df['Close'].values
    
    # Create a time series for the x-axis
    time_series = np.arange(len(prices)).reshape(-1, 1)
    
    # Fit a linear regression model
    model = LinearRegression()
    model.fit(time_series, prices)
    
    # Predict the next 7 days
    future_time_series = np.arange(len(prices), len(prices) + 7).reshape(-1, 1)
    predicted_prices = model.predict(future_time_series)
    
    # Plot the data
    fig, ax = plt.subplots()
    ax.plot(df.index, prices, label='Historical Prices')
    ax.plot(df.index[-1] + pd.DateOffset(days=1), predicted_prices, label='Predicted Prices', linestyle='--')
    ax.set_xlabel('Date')
    ax.set_ylabel('Stock Price')
    ax.set_title('Stock Price Prediction')
    ax.legend()
    
    return predicted_prices, ax