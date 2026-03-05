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
    """
    Generate a DataFrame with detailed artificial sensor readings for specified timestamps and sensor statuses from a predefined list.
    The function generates sensor readings for Sensor1, Sensor2, and Sensor3 (or their corresponding named columns in the supplied column list) using sine, cosine, and tan functions, respectively, of the timestamp (converted to seconds), with a small random noise added to simulate real sensor data variability. SensorStatus is randomly chosen from the provided statuses for each timestamp.
    """
    # Set random seed for reproducibility
    np.random.seed(random_seed)

    # Generate timestamps
    timestamps = pd.date_range(start_time, end_time, freq=step)

    # Generate sensor readings
    sensor_readings = []
    for timestamp in timestamps:
        # Convert timestamp to seconds
        seconds = (timestamp - datetime(1970, 1, 1)).total_seconds()

        # Generate sensor readings for each sensor
        sensor_readings.append({
            "Timestamp": timestamp,
            "Sensor1": math.sin(seconds) + np.random.normal(0, 0.1),
            "Sensor2": math.cos(seconds) + np.random.normal(0, 0.1),
            "Sensor3": math.tan(seconds) + np.random.normal(0, 0.1),
            "SensorStatus": np.random.choice(sensor_statuses)
        })

    # Create DataFrame
    df = pd.DataFrame(sensor_readings, columns=columns)

    return df