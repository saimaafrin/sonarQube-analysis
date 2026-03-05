
import numpy as np
import pandas as pd
from datetime import datetime

def task_func(days_in_past=7, stock_names=["AAPL", "GOOGL", "MSFT", "AMZN", "FB"], random_seed=0):
    np.random.seed(random_seed)
    prices = np.random.rand(days_in_past, len(stock_names))
    dates = [datetime.today() - pd.Timedelta(days=i) for i in range(days_in_past)]
    df = pd.DataFrame(
        {
            "Date": dates,
            "AAPL": prices[:, 0],
            "GOOGL": prices[:, 1],
            "MSFT": prices[:, 2],
            "AMZN": prices[:, 3],
            "FB": prices[:, 4],
        }
    )
    return df