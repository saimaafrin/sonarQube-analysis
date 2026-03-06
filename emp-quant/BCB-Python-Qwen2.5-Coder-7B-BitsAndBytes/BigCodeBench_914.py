
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def task_func(df):
    # Ensure the dataframe has at least two columns: 'timestamp' and 'price'
    if 'timestamp' not in df.columns or 'price' not in df.columns:
        raise ValueError("DataFrame must contain 'timestamp' and 'price' columns.")
    
    # Convert timestamp column to datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
    
    # Set the timestamp as the index
    df.set_index('timestamp', inplace=True)
    
    # Fit a linear regression model
    X = df.index.values.reshape(-1, 1)  # Reshape to be a 2D array
    y = df['price'].values
    model = LinearRegression()
    model.fit(X, y)
    
    # Predict the next 7 days
    last_timestamp = df.index[-1]
    future_timestamps = pd.date_range(start=last_timestamp, periods=8, freq='D')[1:]  # Exclude the last one which is the current day
    future_X = future_timestamps.values.reshape(-1, 1)
    predicted_prices = model.predict(future_X)
    
    # Plotting
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df.index, df['price'], label='Historical Prices')
    ax.plot(future_timestamps, predicted_prices, label='Predicted Prices', linestyle='--')
    ax.set_xlabel('Date')
    ax.set_ylabel('Stock Price')
    ax.set_title('Stock Price Prediction Using Linear Regression')
    ax.legend()
    
    return (predicted_prices.tolist(), ax)