import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def task_func(start_date: str, periods: int, freq: str, random_seed: int = 0) -> (pd.DataFrame, plt.Axes):
    """
    Generates and plots a sales forecast starting from a given date, for a specified number of periods and frequency.

    Args:
        start_date (str): The start date of the forecast.
        periods (int): The number of periods to forecast.
        freq (str): The frequency of the forecast.
        random_seed (int, optional): The random seed to use for the forecast. Defaults to 0.

    Returns:
        A tuple containing:
            1. A DataFrame with columns ['Date', 'Sales'], where 'Date' is the forecast date and 'Sales' are the forecasted sales.
            2. A matplotlib Axes object for the sales forecast plot.
    """
    # Set random seed
    np.random.seed(random_seed)

    # Generate random sales data
    sales_data = np.random.normal(100, 10, size=(periods,))

    # Create DataFrame with forecast data
    forecast_data = pd.DataFrame({'Date': pd.date_range(start=start_date, periods=periods, freq=freq),
                                  'Sales': sales_data})

    # Plot forecast data
    fig, ax = plt.subplots()
    ax.plot(forecast_data['Date'], forecast_data['Sales'])
    ax.set_xlabel('Date')
    ax.set_ylabel('Sales')
    ax.set_title('Sales Forecast')

    return forecast_data, ax
start_date = '2022-01-01'
periods = 10
freq = 'M'
random_seed = 0