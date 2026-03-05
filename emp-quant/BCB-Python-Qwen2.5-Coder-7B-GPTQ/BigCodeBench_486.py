from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def task_func(start_time, end_time, step, trend, seed=42):
    """
    Generate a time series with a specified start time, end time, step, and trend.
    
    Parameters:
    - start_time (datetime): The start time of the time series.
    - end_time (datetime): The end time of the time series.
    - step (int): The time step in seconds.
    - trend (float): The linear trend to be added to the time series.
    - seed (int): The seed for the random number generator.
    
    Returns:
    - ax (matplotlib.pyplot.Axes): The Axes object of the generated plot.
    """
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Generate time points
    time_points = pd.date_range(start=start_time, end=end_time, freq=f'{step}S')
    
    # Generate random values from a normal distribution
    values = np.random.randn(len(time_points))
    
    # Add linear trend
    values += trend * np.arange(len(time_points))
    
    # Create a DataFrame to hold the time series data
    df = pd.DataFrame({'Time': time_points, 'Value': values})
    
    # Plot the time series
    fig, ax = plt.subplots()
    ax.plot(df['Time'], df['Value'], label='Time Series')
    ax.set_xlabel('Time')
    ax.set_ylabel('Value')
    ax.set_title('Generated Time Series with Trend')
    ax.legend()
    
    return ax
start_time = datetime(2023, 1, 1)
end_time = datetime(2023, 1, 2)
step = 3600
trend = 0.1