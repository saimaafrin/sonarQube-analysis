import pandas as pd
from datetime import datetime, timedelta
import random
import matplotlib.pyplot as plt
def task_func(start_date, end_date, num_series, seed=None):
    """
    Generates a DataFrame with multiple random integer time series and plots them.

    Parameters:
    start_date (str): The start date in 'YYYY-MM-DD' format.
    end_date (str): The end date in 'YYYY-MM-DD' format.
    num_series (int): The number of time series to generate.
    seed (int, optional): The seed for the random number generator.

    Returns:
    pandas.DataFrame: A DataFrame containing the generated time series.
    plt.Axes: A matplotlib line plot of the time series.
    """
    # Validate input parameters
    if start_date > end_date:
        raise ValueError("start_date must be earlier than end_date")
    if num_series < 1:
        raise ValueError("num_series must be at least 1")

    # Set the random seed if provided
    if seed is not None:
        random.seed(seed)

    # Convert start and end dates to datetime objects
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')

    # Calculate the number of days between start and end date
    num_days = (end_date - start_date).days + 1

    # Initialize an empty DataFrame with the date range as the index
    date_range = pd.date_range(start=start_date, periods=num_days)
    df = pd.DataFrame(index=date_range)

    # Generate random integer time series for each series
    for i in range(num_series):
        series_name = f"series_{i+1}"
        df[series_name] = [random.randint(0, 100) for _ in range(num_days)]

    # Plot the time series
    ax = df.plot(title="Random Time Series", xlabel="Date", ylabel="Value")
    ax.legend(title="Series")

    return df, ax