
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(start_date: str, periods: int, freq: str, random_seed: int = 0) -> (pd.DataFrame, plt.Axes):
    # Generate a random sales forecast
    np.random.seed(random_seed)
    sales_forecast = np.random.normal(100, 10, size=periods)

    # Create a DataFrame with the forecast data
    forecast_df = pd.DataFrame({'Date': pd.date_range(start=start_date, periods=periods, freq=freq),
                               'Sales': sales_forecast})

    # Plot the sales forecast
    fig, ax = plt.subplots()
    ax.plot(forecast_df['Date'], forecast_df['Sales'])
    ax.set_xlabel('Date')
    ax.set_ylabel('Sales')
    ax.set_title('Sales Forecast')

    return (forecast_df, ax)