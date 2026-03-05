
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def task_func(df):
    # Ensure the dataframe has a datetime index
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    
    # Extract the closing prices
    prices = df['close'].values
    
    # Create a time index in seconds
    time_index = np.arange(len(prices)) * 24 * 60 * 60
    
    # Reshape the time index for the model
    time_index = time_index.reshape(-1, 1)
    
    # Fit the linear regression model
    model = LinearRegression()
    model.fit(time_index, prices)
    
    # Predict the next 7 days
    future_time_index = np.arange(len(prices), len(prices) + 7) * 24 * 60 * 60
    future_time_index = future_time_index.reshape(-1, 1)
    predicted_prices = model.predict(future_time_index)
    
    # Plot the data
    fig, ax = plt.subplots()
    ax.plot(df.index, prices, label='Historical Prices')
    ax.plot(pd.date_range(start=df.index[-1], periods=8, closed='right'), predicted_prices, label='Predicted Prices', linestyle='--')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.set_title('Stock Price Prediction')
    ax.legend()
    
    return predicted_prices, ax