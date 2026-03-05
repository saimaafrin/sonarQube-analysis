
import pandas as pd
from datetime import datetime
import random

def task_func(start_date, end_date, num_series, seed=None):
    if start_date > end_date:
        raise ValueError("Start date cannot be later than end date")
    if num_series < 1:
        raise ValueError("Number of series must be greater than 0")
    if seed is None:
        random.seed(0)
    dates = pd.date_range(start_date, end_date)
    series = []
    for i in range(num_series):
        series.append(random.randint(0, 100))
    df = pd.DataFrame(series, index=dates, columns=["series_{}".format(i)])
    fig, ax = plt.subplots()
    ax.plot(df.index, df.values, label="Random Time Series")
    ax.set_xlabel("Date")
    ax.set_ylabel("Value")
    ax.legend()
    return df, fig