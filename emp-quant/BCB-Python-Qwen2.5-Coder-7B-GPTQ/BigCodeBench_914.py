import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
def task_func(df):
    # Convert the 'timestamp' column to datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    # Set the 'timestamp' column as the index
    df.set_index('timestamp', inplace=True)
    
    # Create a new column 'time_in_seconds' to represent time in seconds since the first timestamp
    df['time_in_seconds'] = (df.index - df.index[0]).total_seconds()
    
    # Prepare the features and target variable
    X = df[['time_in_seconds']]
    y = df['close']
    
    # Create and fit the linear regression model
    model = LinearRegression()
    model.fit(X, y)
    
    # Generate future timestamps for the next 7 days
    last_timestamp = df.index[-1]
    future_timestamps = pd.date_range(start=last_timestamp, periods=8, closed='right')[1:]  # Exclude the last timestamp
    future_time_in_seconds = (future_timestamps - df.index[0]).total_seconds()
    
    # Predict the stock prices for the future timestamps
    future_prices = model.predict(future_time_in_seconds.reshape(-1, 1))
    
    # Plot the original data and the predicted data
    fig, ax = plt.subplots()
    ax.plot(df.index, df['close'], label='Actual Prices')
    ax.plot(future_timestamps, future_prices, label='Predicted Prices', linestyle='--')
    ax.set_xlabel('Time')
    ax.set_ylabel('Stock Price')
    ax.set_title('Stock Price Prediction')
    ax.legend()
    
    return future_prices.tolist(), ax