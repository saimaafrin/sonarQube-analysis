
import pandas as pd
from datetime import datetime, timedelta
import random
import matplotlib.pyplot as plt

def task_func(start_date, end_date, num_series, seed=None):
    """
    Generates a DataFrame with multiple random integer time series and plots them.

    Parameters:
    - start_date (str): Start date in 'YYYY-MM-DD' format.
    - end_date (str): End date in 'YYYY-MM-DD' format.
    - num_series (int): Number of time series to generate.
    - seed (int, optional): Seed for random number generation.

    Returns:
    - pd.DataFrame: DataFrame containing the generated time series.
    - plt.Axes: Matplotlib axes object containing the line plot.
    """
    # Validate input parameters
    if start_date > end_date:
        raise ValueError("start_date must be earlier than end_date")
    if num_series < 1:
        raise ValueError("num_series must be at least 1")

    # Set random seed if provided
    if seed is not None:
        random.seed(seed)

    # Convert string dates to datetime objects
    start = datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.strptime(end_date, '%Y-%m-%d')

    # Calculate the number of days between start and end date
    delta = end - start + timedelta(days=1)
    days = [start + timedelta(days=i) for i in range(delta.days)]

    # Initialize an empty dictionary to store the time series data
    data = {}

    # Generate random integer time series for each series
    for i in range(num_series):
        values = [random.randint(0, 100) for _ in days]
        data[f'series_{i+1}'] = values

    # Create a DataFrame from the time series data
    df = pd.DataFrame(data, index=days)

    # Plot the time series
    fig, ax = plt.subplots()
    for col in df.columns:
        ax.plot(df.index, df[col], label=col)

    # Set plot properties
    ax.set_title('Random Time Series')
    ax.set_xlabel('Date')
    ax.set_ylabel('Value')
    ax.legend()

    return df, ax