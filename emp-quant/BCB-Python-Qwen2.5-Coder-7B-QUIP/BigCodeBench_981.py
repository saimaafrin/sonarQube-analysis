
import pandas as pd
from datetime import datetime
import random
import matplotlib.pyplot as plt

def task_func(start_date, end_date, num_series, seed=None):
    # Validate the input parameters
    if start_date > end_date:
        raise ValueError("Start date must be earlier than end date.")
    if num_series < 1:
        raise ValueError("Number of series must be at least 1.")

    # Set the random seed if provided
    if seed is not None:
        random.seed(seed)

    # Generate the time series
    date_range = pd.date_range(start=start_date, end=end_date)
    time_series = pd.DataFrame(index=date_range)

    for i in range(num_series):
        time_series[f"series_{i}"] = [random.randint(0, 100) for _ in range(len(date_range))]

    # Plot the time series
    plt.figure(figsize=(10, 6))
    for i in range(num_series):
        plt.plot(time_series.index, time_series[f"series_{i}"], label=f"series_{i}")

    plt.title("Random Time Series")
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.legend()
    plt.show()

    return time_series, plt.gca()