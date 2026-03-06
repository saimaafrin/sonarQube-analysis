
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
    
    # Generate timestamps
    timestamps = pd.date_range(start=start_time, end=end_time, freq=f'{step}S')
    
    # Initialize data dictionary
    data = {col: [] for col in columns}
    
    for ts in timestamps:
        # Convert timestamp to seconds since epoch
        time_in_seconds = ts.timestamp()
        
        # Calculate sensor readings
        sensor1_reading = math.sin(time_in_seconds) + np.random.normal(0, 0.1)
        sensor2_reading = math.cos(time_in_seconds) + np.random.normal(0, 0.1)
        sensor3_reading = math.tan(time_in_seconds) + np.random.normal(0, 0.1)
        
        # Randomly choose sensor status
        sensor_status = np.random.choice(sensor_statuses)
        
        # Append data to dictionary
        data['Timestamp'].append(ts)
        data['Sensor1'].append(sensor1_reading)
        data['Sensor2'].append(sensor2_reading)
        data['Sensor3'].append(sensor3_reading)
        data['SensorStatus'].append(sensor_status)
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    return df