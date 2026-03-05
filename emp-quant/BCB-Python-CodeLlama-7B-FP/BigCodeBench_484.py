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
    # Generate timestamps
    timestamps = pd.date_range(start_time, end_time, freq=step)

    # Generate sensor readings
    sensor_readings = []
    for timestamp in timestamps:
        sensor_reading = {}
        for column in columns:
            if column == "Timestamp":
                sensor_reading[column] = timestamp
            elif column == "SensorStatus":
                sensor_reading[column] = np.random.choice(sensor_statuses, p=[0.5, 0.3, 0.2])
            else:
                sensor_reading[column] = math.sin(timestamp.timestamp() * 2 * math.pi) + np.random.normal(0, 0.1)
        sensor_readings.append(sensor_reading)

    # Create DataFrame
    df = pd.DataFrame(sensor_readings)

    # Set index
    df.set_index("Timestamp", inplace=True)

    return df