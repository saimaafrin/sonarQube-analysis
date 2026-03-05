import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def task_func(start_date: str, periods: int, freq: str, random_seed: int = 0) -> (pd.DataFrame, plt.Axes):
    """
    Generates and plots a sales forecast starting from a given date, for a specified number of periods and frequency.
    
    Parameters:
    - start_date (str): The starting date for the forecast in 'YYYY-MM-DD' format.
    - periods (int): The number of periods to forecast.
    - freq (str): The frequency of the forecast ('D' for daily, 'W' for weekly, 'M' for monthly).
    - random_seed (int): The random seed for reproducibility.
    
    Returns:
    - A tuple containing:
        1. A DataFrame with columns ['Date', 'Sales'], where 'Date' is the forecast date and 'Sales' are the forecasted sales.
        2. A matplotlib Axes object for the sales forecast plot.
    """
    # Set the random seed for reproducibility
    np.random.seed(random_seed)
    
    # Create a date range
    date_range = pd.date_range(start=start_date, periods=periods, freq=freq)
    
    # Generate random sales data
    sales_data = np.random.randint(100, 1000, size=periods)
    
    # Create a DataFrame
    forecast_df = pd.DataFrame({'Date': date_range, 'Sales': sales_data})
    
    # Plot the sales forecast
    fig, ax = plt.subplots()
    ax.plot(forecast_df['Date'], forecast_df['Sales'], marker='o')
    ax.set_xlabel('Date')
    ax.set_ylabel('Sales')
    ax.set_title('Sales Forecast')
    
    return forecast_df, ax