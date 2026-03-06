
from datetime import datetime
import pandas as pd
import numpy as np

def task_func(start_time, end_time, step, trend, seed=42):
    """
    Generates a time series with a specified trend and plots it.

    Parameters:
    - start_time (str): Start time in ISO format.
    - end_time (str): End time in ISO format.
    - step (int): Step size in seconds between each data point.
    - trend (float): Linear trend value to be added to the time series.
    - seed (int): Seed for random number generation.

    Returns:
    - ax (matplotlib.pyplot.Axes): The Axes object of the generated plot.
    """
    # Convert start and end times to datetime objects
    start = datetime.fromisoformat(start_time)
    end = datetime.fromisoformat(end_time)

    # Generate time points
    time_points = pd.date_range(start=start, end=end, freq=f'{step}S')

    # Set random seed for reproducibility
    np.random.seed(seed)

    # Generate normally distributed values
    values = np.random.normal(size=len(time_points))

    # Add linear trend
    values += trend * np.arange(len(time_points))

    # Create DataFrame
    df = pd.DataFrame({'Time': time_points, 'Value': values})

    # Plotting
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.plot(df['Time'], df['Value'])
    ax.set_xlabel('Time')
    ax.set_ylabel('Value')

    return ax