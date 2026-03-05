import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
def task_func(df):
    # Generate future timestamps
    timestamps = [df.index[-1] + np.timedelta64(24*60*60, 's') for _ in range(7)]

    # Create a new dataframe with the future timestamps
    future_df = pd.DataFrame(index=timestamps)

    # Fill the new dataframe with the last known prices
    future_df['Close'] = df['Close'].iloc[-1]

    # Create a linear regression model
    model = LinearRegression()

    # Train the model on the historical data
    model.fit(df[['Close']], df['Close'])

    # Make predictions on the future data
    predictions = model.predict(future_df[['Close']])

    # Create a list of predicted prices
    predicted_prices = [prediction[0] for prediction in predictions]

    # Plot the data
    ax = df['Close'].plot(label='Actual')
    future_df['Close'].plot(label='Predicted', ax=ax)
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend()

    # Return the tuple
    return (predicted_prices, ax)
df = pd.read_csv('data.csv', index_col='Date', parse_dates=True)