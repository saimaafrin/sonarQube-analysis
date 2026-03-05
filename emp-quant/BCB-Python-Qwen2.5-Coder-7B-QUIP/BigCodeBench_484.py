
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
    # Initialize the random seed for reproducibility
    np.random.seed(random_seed)
    
    # Generate a range of timestamps
    timestamps = pd.date_range(start=start_time, end=end_time, freq=step)
    
    # Generate sensor readings for each timestamp
    sensor1 = np.sin(timestamps.astype(int).astype('timedelta64[s]'))
    sensor2 = np.cos(timestamps.astype(int).astype('timedelta64[s]'))
    sensor3 = np.tan(timestamps.astype(int).astype('timedelta64[s]'))
    
    # Add random noise to the sensor readings
    sensor1 += np.random.uniform(-0.1, 0.1, size=len(sensor1))
    sensor2 += np.random.uniform(-0.1, 0.1, size=len(sensor2))
    sensor3 += np.random.uniform(-0.1, 0.1, size=len(sensor3))
    
    # Generate random sensor statuses
    sensor_statuses = np.random.choice(sensor_statuses, size=len(timestamps))
    
    # Create a DataFrame with the generated data
    data = {
        "Timestamp": timestamps,
        "Sensor1": sensor1,
        "Sensor2": sensor2,
        "Sensor3": sensor3,
        "SensorStatus": sensor_statuses
    }
    
    # Create the DataFrame
    df = pd.DataFrame(data)
    
    return df