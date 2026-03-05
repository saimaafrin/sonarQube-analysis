
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def task_func(df):
    # Ensure the dataframe has at least one column for prediction
    if 'Close' not in df.columns:
        raise ValueError("DataFrame must contain a 'Close' column for prediction.")

    # Convert the index to datetime if not already
    if not isinstance(df.index, pd.DatetimeIndex):
        df.index = pd.to_datetime(df.index)

    # Split the data into training and testing sets
    train_size = int(len(df) * 0.8)
    train, test = df.iloc[:train_size], df.iloc[train_size:]

    # Prepare the features and target for the model
    X_train = train.index.values.reshape(-1, 1)
    y_train = train['Close'].values

    X_test = test.index.values.reshape(-1, 1)
    y_test = test['Close'].values

    # Initialize and train the linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict future prices
    future_dates = pd.date_range(start=df.index[-1], periods=8, freq='D')[1:]
    future_dates = future_dates.values.reshape(-1, 1)
    future_predictions = model.predict(future_dates)

    # Plot the data
    fig, ax = plt.subplots()
    ax.plot(df.index, df['Close'], label='Actual Prices')
    ax.plot(future_dates, future_predictions, label='Predicted Prices', color='orange')
    ax.set_xlabel('Date')
    ax.set_ylabel('Close Price')
    ax.set_title('Stock Price Prediction')
    ax.legend()

    # Return the list of predicted prices and the plot
    return (future_predictions.tolist(), ax)