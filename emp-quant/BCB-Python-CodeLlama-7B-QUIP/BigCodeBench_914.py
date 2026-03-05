
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def task_func(df):
    # Calculate the slope and intercept of the linear regression
    slope, intercept = np.polyfit(df['date'], df['close'], 1)
    # Generate the predicted prices for the next 7 days
    predicted_prices = [slope * (i + 1) + intercept for i in range(7)]
    # Plot the data
    fig, ax = plt.subplots()
    ax.plot(df['date'], df['close'])
    ax.plot(predicted_prices)
    ax.set_xlabel('Date')
    ax.set_ylabel('Close')
    ax.set_title('Stock Closing Prices')
    plt.show()
    return (predicted_prices, ax)