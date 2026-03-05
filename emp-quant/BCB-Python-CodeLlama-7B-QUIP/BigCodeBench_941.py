
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(start_date: str, periods: int, freq: str, random_seed: int = 0) -> (pd.DataFrame, plt.Axes):
    # Create a pandas DataFrame with the given start date and number of periods
    df = pd.DataFrame({'Date': pd.date_range(start_date, periods=periods, freq=freq)},
                      columns=['Date', 'Sales'])

    # Generate random sales data for the given number of periods
    np.random.seed(random_seed)
    df['Sales'] = np.random.normal(1000, 100, periods)

    # Plot the sales forecast
    fig, ax = plt.subplots()
    ax.plot(df['Date'], df['Sales'])
    ax.set_xlabel('Date')
    ax.set_ylabel('Sales')
    ax.set_title('Sales Forecast')
    return df, ax