
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
    # Generate timestamps
    timestamps = pd.date_range(start_time, end_time, freq=step)

    # Generate sensor readings
    sensor_readings = []
    for timestamp in timestamps:
        # Generate random sensor status
        sensor_status = np.random.choice(sensor_statuses, p=[0.5, 0.3, 0.2])

        # Generate sensor readings for each sensor
        sensor_readings_for_sensor = []
        for sensor_name in columns[1:]:
            # Generate random noise
            noise = np.random.normal(0, 0.1, size=1)

            # Generate sensor reading
            if sensor_name == "Sensor1":
                reading = math.sin(timestamp.timestamp() * 2 * math.pi) + noise
            elif sensor_name == "Sensor2":
                reading = math.cos(timestamp.timestamp() * 2 * math.pi) + noise
            elif sensor_name == "Sensor3":
                reading = math.tan(timestamp.timestamp() * 2 * math.pi) + noise
            else:
                raise ValueError(f"Invalid sensor name: {sensor_name}")

            # Add sensor reading to list
            sensor_readings_for_sensor.append(reading)

        # Add sensor readings to list
        sensor_readings.append(sensor_readings_for_sensor)

    # Create DataFrame
    df = pd.DataFrame(sensor_readings, columns=columns)

    # Add timestamp column
    df["Timestamp"] = timestamps

    # Add sensor status column
    df["SensorStatus"] = sensor_statuses

    return df