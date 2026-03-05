import numpy as np
import pandas as pd
from datetime import datetime, timedelta
def task_func(
    days_in_past=7, stock_names=["AAPL", "GOOGL", "MSFT", "AMZN", "FB"], random_seed=0
):
    """
    Generates a DataFrame of random stock prices for a specified number of days in the past.

    Parameters:
    days_in_past (int): The number of days in the past for which to generate stock prices.
    stock_names (list): A list of stock names to include in the DataFrame.
    random_seed (int): The seed for the random number generator for reproducibility.

    Returns:
    pandas.DataFrame: A DataFrame containing random stock prices for the specified number of days.
    """
    # Set the random seed for reproducibility
    np.random.seed(random_seed)
    
    # Create a date range for the specified number of days in the past
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days_in_past)
    date_range = pd.date_range(start=start_date, end=end_date)
    
    # Create a DataFrame with random stock prices
    stock_prices = pd.DataFrame(index=date_range, columns=stock_names)
    for stock in stock_names:
        stock_prices[stock] = np.random.rand(days_in_past)
    
    return stock_prices