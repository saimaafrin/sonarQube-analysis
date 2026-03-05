import pandas as pd
from datetime import datetime
import random
def task_func(start_date, end_date, num_series, seed=None):
    """
    Generates a DataFrame with multiple random integer time series (each ranging from 0 to 100) from a start date to an end date, then returns the generated time series on a line plot.
    """
    if start_date > end_date:
        raise ValueError("Start date cannot be later than end date")
    if num_series < 1:
        raise ValueError("Number of series must be greater than 0")

    # Generate random time series
    time_series = []
    for i in range(num_series):
        series = []
        for date in pd.date_range(start_date, end_date):
            series.append(random.randint(0, 100))
        time_series.append(series)

    # Create DataFrame
    df = pd.DataFrame(time_series, index=pd.date_range(start_date, end_date))

    # Plot time series
    fig, ax = plt.subplots()
    for i, series in enumerate(time_series):
        ax.plot(df.index, series, label=f"series_{i}")
    ax.set_title("Random Time Series")
    ax.set_xlabel("Date")
    ax.set_ylabel("Value")
    ax.legend()
    return df, ax