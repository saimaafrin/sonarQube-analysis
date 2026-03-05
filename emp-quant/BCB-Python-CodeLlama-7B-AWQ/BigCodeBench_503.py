import numpy as np
import pandas as pd
from datetime import datetime
def task_func(
    days_in_past=7, stock_names=["AAPL", "GOOGL", "MSFT", "AMZN", "FB"], random_seed=0
):
    """
    Create a DataFrame of stock prices for a specified number of days in the past using random data.

    Args:
        days_in_past (int): The number of days in the past for which to generate stock prices.
        stock_names (list): A list of stock names to use for the DataFrame.
        random_seed (int): The random seed to use for generating random stock prices.

    Returns:
        DataFrame: A pandas DataFrame containing random stock prices for the specified number of days.
    """
    np.random.seed(random_seed)
    stock_prices = np.random.uniform(0.0, 1.0, size=(days_in_past, len(stock_names)))
    stock_prices = pd.DataFrame(stock_prices, columns=stock_names)
    stock_prices.index = pd.date_range(
        start=datetime.now() - pd.Timedelta(days=days_in_past),
        periods=days_in_past,
        freq="D",
    )
    return stock_prices