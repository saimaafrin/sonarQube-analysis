
import pandas as pd
from datetime import datetime
import random
import matplotlib.pyplot as plt

def task_func(start_date, end_date, num_series, seed=None):
    if start_date > end_date:
        raise ValueError("Start date cannot be later than end date")
    if num_series < 1:
        raise ValueError("Number of series must be greater than 0")

    # Generate random time series
    time_series = []
    for i in range(num_series):
        series = []
        for date in pd.date_range(start_date, end_date):
            value = random.randint(0, 100)
            series.append((date, value))
        time_series.append(series)

    # Create DataFrame and plot
    df = pd.DataFrame(time_series, columns=["Date", "Value"])
    df.set_index("Date", inplace=True)
    ax = df.plot(kind="line", title="Random Time Series", xlabel="Date", ylabel="Value")
    for i, series in enumerate(time_series):
        ax.plot(series, label=f"Series {i}")
    ax.legend()

    return df, ax