import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
def task_func(df):
    # Ensure the dataframe has a datetime index
    df.index = pd.to_datetime(df.index)
    
    # Prepare the data for the model
    X = df.index.values.reshape(-1, 1)
    y = df['Close'].values
    
    # Fit the linear regression model
    model = LinearRegression()
    model.fit(X, y)
    
    # Generate future timestamps for the next 7 days
    future_dates = pd.date_range(start=df.index[-1], periods=8, freq='D')[1:]
    future_X = future_dates.values.reshape(-1, 1)
    
    # Predict the stock prices for the next 7 days
    predicted_prices = model.predict(future_X)
    
    # Plot the original data and the predicted prices
    fig, ax = plt.subplots()
    ax.plot(df.index, df['Close'], label='Historical Prices')
    ax.plot(future_dates, predicted_prices, label='Predicted Prices', linestyle='--')
    ax.set_xlabel('Date')
    ax.set_ylabel('Stock Price')
    ax.set_title('Stock Price Prediction')
    ax.legend()
    
    return predicted_prices, ax