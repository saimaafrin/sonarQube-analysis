
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(start_time, end_time, step, trend, seed=42):
    np.random.seed(seed)
    time_series = pd.date_range(start_time, end_time, freq=step)
    values = np.random.normal(size=len(time_series))
    trend_values = np.linspace(0, trend, len(time_series))
    values = values + trend_values
    ax = plt.plot(time_series, values)
    ax.set_xlabel('Time')
    ax.set_ylabel('Value')
    return ax