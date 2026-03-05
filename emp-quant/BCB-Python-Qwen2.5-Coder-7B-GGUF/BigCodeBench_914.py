
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def task_func(df):
    # Ensure the dataframe has the necessary columns
    if 'timestamp' not in df.columns or 'price' not in df.columns:
        raise ValueError("DataFrame must contain 'timestamp' and 'price' columns")
    
    # Convert timestamp to datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
    
    # Sort the dataframe by timestamp
    df = df.sort_values(by='timestamp')
    
    # Prepare the data for the model
    X = df['timestamp'].values.reshape(-1, 1)
    y = df['price'].values
    
    # Create and fit the linear regression model
    model = LinearRegression()
    model.fit(X, y)
    
    # Predict the next 7 days
    future_timestamps = np.array([df['timestamp'].iloc[-1] + pd.Timedelta(days=i) for i in range(1, 8)]).reshape(-1, 1)
    predicted_prices = model.predict(future_timestamps)
    
    # Plot the data
    fig, ax = plt.subplots()
    ax.plot(df['timestamp'], df['price'], label='Historical Prices')
    ax.plot(future_timestamps, predicted_prices, label='Predicted Prices', linestyle='--')
    ax.set_xlabel('Timestamp')
    ax.set_ylabel('Price')
    ax.set_title('Stock Price Prediction')
    ax.legend()
    
    return predicted_prices, ax