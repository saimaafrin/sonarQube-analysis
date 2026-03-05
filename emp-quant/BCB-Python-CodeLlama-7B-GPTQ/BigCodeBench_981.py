import pandas as pd
from datetime import datetime
import random
def task_func(start_date, end_date, num_series, seed=None):
    """
    Generates a DataFrame with multiple random integer time series (each ranging from 0 to 100) from a start date to an end date, then returns the generated time series on a line plot.

    Parameters
    ----------
    start_date : datetime.datetime
        Start date of the time series.
    end_date : datetime.datetime
        End date of the time series.
    num_series : int
        Number of time series to generate.
    seed : int, optional
        Random seed for reproducibility.

    Returns
    -------
    pandas.DataFrame
        A pandas DataFrame containing the generated time series, indexed by date.
    plt.Axes
        A matplotlib line plot of the time series.

    Raises
    ------
    ValueError
        If start_date is later than end_date.
        If num_series is less than 1.
    """
    if start_date > end_date:
        raise ValueError("Start date cannot be later than end date.")
    if num_series < 1:
        raise ValueError("Number of series must be greater than 0.")

    # Generate random time series
    time_series = []
    for i in range(num_series):
        series = []
        for date in pd.date_range(start_date, end_date):
            value = random.randint(0, 100)
            series.append((date, value))
        time_series.append(series)

    # Create DataFrame
    df = pd.DataFrame(time_series, columns=["Date", "Value"])
    df.set_index("Date", inplace=True)

    # Plot time series
    fig, ax = plt.subplots()
    for i, series in enumerate(time_series):
        ax.plot(series, label=f"Series {i}")
    ax.set_title("Random Time Series")
    ax.set_xlabel("Date")
    ax.set_ylabel("Value")
    ax.legend()

    return df, ax