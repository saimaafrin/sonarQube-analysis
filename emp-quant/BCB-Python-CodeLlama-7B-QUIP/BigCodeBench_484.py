
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
    # Generate a list of timestamps
    timestamps = pd.date_range(start_time, end_time, step)

    # Generate a list of sensor readings
    sensor_readings = []
    for timestamp in timestamps:
        # Generate a random sensor reading for each sensor
        sensor1 = math.sin(timestamp.timestamp()) + np.random.normal(0, 0.1)
        sensor2 = math.cos(timestamp.timestamp()) + np.random.normal(0, 0.1)
        sensor3 = math.tan(timestamp.timestamp()) + np.random.normal(0, 0.1)

        # Generate a random sensor status
        sensor_status = np.random.choice(sensor_statuses, 1)

        # Add the sensor reading and status to the list
        sensor_readings.append([timestamp, sensor1, sensor2, sensor3, sensor_status])

    # Create a DataFrame from the list of sensor readings
    df = pd.DataFrame(sensor_readings, columns=columns)

    return df