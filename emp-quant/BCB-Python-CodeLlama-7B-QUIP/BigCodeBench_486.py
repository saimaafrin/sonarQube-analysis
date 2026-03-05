
from datetime import datetime
import pandas as pd
import numpy as np

def task_func(start_time, end_time, step, trend, seed=42):
    np.random.seed(seed)
    time_series = pd.Series(np.random.normal(0, 1, size=int((end_time - start_time) / step)) + trend * np.arange(start_time, end_time, step))
    fig, ax = plt.subplots()
    ax.plot(time_series.index, time_series.values)
    ax.set_xlabel('Time')
    ax.set_ylabel('Value')
    return ax