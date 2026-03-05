from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def task_func(start_time, end_time, step, trend, seed=42):
    """
    Generates a time series with a specified start time, end time, step, and trend.
    The values are generated from a normal distribution and a linear trend is added.
    
    Parameters:
    - start_time (str): The start time in 'YYYY-MM-DD HH:MM:SS' format.
    - end_time (str): The end time in 'YYYY-MM-DD HH:MM:SS' format.
    - step (int): The time step in seconds.
    - trend (float): The linear trend value to be added to the time series.
    - seed (int): The random seed for reproducibility.
    
    Returns:
    - ax (matplotlib.pyplot.Axes): The Axes object of the generated plot.
    """
    # Convert start and end times to datetime objects
    start = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
    end = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
    
    # Generate time series
    time_series = pd.date_range(start=start, end=end, freq=f'{step}S')
    values = np.random.normal(size=len(time_series)) + trend * np.arange(len(time_series))
    
    # Create DataFrame
    df = pd.DataFrame({'Time': time_series, 'Value': values})
    
    # Plotting
    fig, ax = plt.subplots()
    ax.plot(df['Time'], df['Value'], label='Time Series')
    ax.set_xlabel('Time')
    ax.set_ylabel('Value')
    ax.set_title('Generated Time Series')
    ax.legend()
    
    return ax
start_time = '2023-01-01 00:00:00'
end_time = '2023-01-01 00:01:00'
step = 10
trend = 0.1