
import numpy as np
import pandas as pd
from datetime import datetime

def task_func(
    days_in_past=7, stock_names=["AAPL", "GOOGL", "MSFT", "AMZN", "FB"], random_seed=0
):
    # Set the random seed for reproducibility
    np.random.seed(random_seed)
    
    # Create a date range for the specified number of days in the past
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days_in_past)
    date_range = pd.date_range(start=start_date, end=end_date)
    
    # Initialize an empty dictionary to store the stock prices
    stock_prices = {}
    
    # Generate random stock prices for each stock name
    for stock_name in stock_names:
        stock_prices[stock_name] = np.random.rand(days_in_past).tolist()
    
    # Create a DataFrame from the stock prices
    df = pd.DataFrame(stock_prices, index=date_range)
    
    return df