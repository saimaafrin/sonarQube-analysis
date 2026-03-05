import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def task_func(start_time, end_time, step, trend, seed=42):
    np.random.seed(seed)
    time_series = []
    for i in range(int((end_time - start_time).total_seconds() / step)):
        time_series.append(start_time + datetime.timedelta(seconds=i * step))
        value = np.random.normal(0, 1) + trend * i
        time_series.append(value)
    df = pd.DataFrame({'Time': time_series, 'Value': value})
    ax = df.plot(x='Time', y='Value', kind='line')
    ax.set_xlabel('Time')
    ax.set_ylabel('Value')
    return ax
start_time = datetime.datetime(2022, 1, 1)
end_time = datetime.datetime(2022, 1, 10)
step = 86400
trend = 1