
import math
import numpy as np
from datetime import datetime
import pandas as pd

def task_func(
    start_time,
    end_time,
    step,
    columns=["Timestamp", "Sensor1", "Sensor2", "Sensor3", "SensorStatus"],
    sensor_statuses=["OK", "MAINTENANCE_REQUIRED", "ERROR"],
    random_seed=42,
):
    np.random.seed(random_seed)
    timestamps = pd.date_range(start=start_time, end=end_time, freq=step)
    sensor1 = np.sin(timestamps.astype(np.int64) / 1e9) + np.random.normal(0, 0.1, len(timestamps))
    sensor2 = np.cos(timestamps.astype(np.int64) / 1e9) + np.random.normal(0, 0.1, len(timestamps))
    sensor3 = np.tan(timestamps.astype(np.int64) / 1e9) + np.random.normal(0, 0.1, len(timestamps))
    sensor_status = np.random.choice(sensor_statuses, size=len(timestamps))
    
    data = {
        "Timestamp": timestamps,
        "Sensor1": sensor1,
        "Sensor2": sensor2,
        "Sensor3": sensor3,
        "SensorStatus": sensor_status
    }
    
    return pd.DataFrame(data)