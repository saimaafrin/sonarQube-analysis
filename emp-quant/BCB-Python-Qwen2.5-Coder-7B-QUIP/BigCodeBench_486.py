
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(start_time, end_time, step, trend, seed=42):
    # Generate a time series with a normal distribution and a linear trend
    np.random.seed(seed)
    time_series = pd.DataFrame({
        'Time': pd.date_range(start=start_time, end=end_time, freq=step),
        'Value': np.random.randn(len(time_series)) * trend
    })

    # Plot the time series
    fig, ax = plt.subplots()
    ax.plot(time_series['Time'], time_series['Value'], label='Value')
    ax.set_xlabel('Time')
    ax.set_ylabel('Value')
    ax.set_title('Time Series with Normal Distribution and Linear Trend')
    ax.legend()

    return ax