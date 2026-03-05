from datetime import datetime
import pandas as pd
import numpy as np
def task_func(start_time, end_time, step, trend, seed=42):
    """
    Generates a time series with a specified start time, end time, step, and trend.
    The values are generated from a normal distribution and a linear trend is added.
    
    Parameters:
    - start_time (datetime): The start time of the time series.
    - end_time (datetime): The end time of the time series.
    - step (int): The time step in seconds.
    - trend (float): The linear trend value to be added to the time series.
    - seed (int): The random seed for reproducibility.
    
    Returns:
    - ax (matplotlib.pyplot.Axes): The Axes object of the generated plot.
    """
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Generate time series data
    time = pd.date_range(start=start_time, end=end_time, freq=f'{step}S')
    values = np.random.normal(loc=0, scale=1, size=len(time)) + trend * np.arange(len(time))
    
    # Create a DataFrame
    df = pd.DataFrame({'Time': time, 'Value': values})
    
    # Plot the time series
    ax = df.plot(x='Time', y='Value', figsize=(10, 5))
    ax.set_xlabel('Time')
    ax.set_ylabel('Value')
    
    return ax