
import math
import numpy as np
from datetime import datetime
import pandas as pd

def task_func(start_time, end_time, step, columns=["Timestamp", "Sensor1", "Sensor2", "Sensor3", "SensorStatus"], sensor_statuses=["OK", "MAINTENANCE_REQUIRED", "ERROR"], random_seed=42):
    # Generate timestamps
    timestamps = pd.date_range(start_time, end_time, freq=step)

    # Generate sensor readings
    sensor_readings = {}
    for sensor in columns[1:]:
        sensor_readings[sensor] = np.sin(timestamps.astype(np.float64) / 1000) + np.random.normal(0, 0.1, size=len(timestamps))

    # Add sensor statuses
    sensor_statuses = np.random.choice(sensor_statuses, size=len(timestamps), p=[0.5, 0.3, 0.2])

    # Create DataFrame
    df = pd.DataFrame(sensor_readings, index=timestamps)
    df["SensorStatus"] = sensor_statuses

    return df

df = task_func(start_time, end_time, step, columns, sensor_statuses, random_seed)
print(df)