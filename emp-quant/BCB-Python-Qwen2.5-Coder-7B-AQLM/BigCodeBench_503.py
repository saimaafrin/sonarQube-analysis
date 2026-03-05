
import numpy as np
import pandas as pd
from datetime import datetime

def task_func(
    days_in_past=7, stock_names=["AAPL", "GOOGL", "MSFT", "AMZN", "FB"], random_seed=0
):
    np.random.seed(random_seed)
    dates = pd.date_range(datetime.now() - pd.Timedelta(days=days_in_past), periods=days_in_past)
    stock_data = {stock: np.random.rand(days_in_past).tolist() for stock in stock_names}
    df = pd.DataFrame(stock_data, index=dates)
    return df