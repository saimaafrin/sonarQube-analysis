
import numpy as np
import pandas as pd
from datetime import datetime

def task_func(days_in_past=7, stock_names=["AAPL", "GOOGL", "MSFT", "AMZN", "FB"], random_seed=0):
    np.random.seed(random_seed)
    dates = pd.date_range(datetime.now() - pd.Timedelta(days=days_in_past), datetime.now())
    prices = np.random.uniform(0.0, 1.0, size=(len(dates), len(stock_names)))
    df = pd.DataFrame(prices, index=dates, columns=stock_names)
    return df