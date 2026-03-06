import pandas as pd
from datetime import datetime
import random
def task_func(start_date, end_date, num_series, seed=None):
    """
    Generates a DataFrame with multiple random integer time series (each ranging
    from 0 to 100) from a start date to an end date, then returns the generated time series
    on a line plot.

    Parameters:
    - start_date (str): The start date in "yyyy-mm-dd" format.
    - end_date (str): The end date in "yyyy-mm-dd" format.
    - num_series (int): The number of random time series to generate.
    - seed (int, optional): Seed for the random number generator. Defaults to None (not set).

    Returns:
    - pandas.DataFrame: A pandas DataFrame containing the generated time series, indexed by date.
    - plt.Axes: A matplotlib line plot of the time series.

    Raises:
    - ValueError: If start_date is later than end_date; or if num_series is less than 1.

    Requirements:
    - pandas
    - datetime
    - random

    Notes:
    - The line plot's title is set to "Random Time Series", the x-axis label to "Date",
      and the y-axis label to "Value".
    - Each time series is plotted as a separate line with automatic coloring and legend
      entry labeled as "series_x" where x is the series number.

    Example:
    >>> df, ax = task_func('2020-01-01', '2020-12-31', 3, 42)
    >>> df.head(2)
                series_1  series_2  series_3
    2020-01-01        81        67        19
    2020-01-02        14        20        29
    """
    if start_date > end_date:
        raise ValueError("start_date must be earlier than end_date")
    if num_series < 1:
        raise ValueError("num_series must be greater than 0")

    # Generate random time series
    if seed is not None:
        random.seed(seed)
    df = pd.DataFrame(index=pd.date_range(start_date, end_date))
    for i in range(num_series):
        df[f"series_{i}"] = random.choices(range(101), k=len(df))

    # Plot the time series
    fig, ax = plt.subplots()
    ax.set_title("Random Time Series")
    ax.set_xlabel("Date")
    ax.set_ylabel("Value")
    for i in range(num_series):
        ax.plot(df.index, df[f"series_{i}"], label=f"series_{i}")
    ax.legend()
    return df, ax