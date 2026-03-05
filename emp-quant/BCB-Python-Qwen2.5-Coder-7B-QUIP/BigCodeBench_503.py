
import numpy as np
import pandas as pd
from datetime import datetime

def task_func(
    days_in_past=7, stock_names=["AAPL", "GOOGL", "MSFT", "AMZN", "FB"], random_seed=0
):
    # Set the random seed for reproducibility
    np.random.seed(random_seed)
    
    # Create a date range for the specified number of days in the past
    date_range = pd.date_range(end=datetime.now(), periods=days_in_past, freq='D')
    
    # Create a DataFrame with random stock prices
    stock_prices = pd.DataFrame(
        np.random.rand(days_in_past, len(stock_names)),
        index=date_range,
        columns=stock_names
    )
    
    return stock_prices