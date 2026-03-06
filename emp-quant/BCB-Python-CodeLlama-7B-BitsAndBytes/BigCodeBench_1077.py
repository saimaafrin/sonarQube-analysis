
from datetime import datetime
import pytz
import numpy as np

def task_func(time_strings, timezone):
    # Convert each timestamp to the specified timezone
    timestamps = [pytz.timezone(timezone).localize(datetime.strptime(time_string, '%Y-%m-%d %H:%M:%S')) for time_string in time_strings]

    # Calculate the absolute time difference in seconds between each consecutive pair of timestamps
    time_differences = [abs(timestamp1 - timestamp2).total_seconds() for timestamp1, timestamp2 in zip(timestamps, timestamps[1:])]

    # Calculate the mean time difference in seconds
    mean_time_difference = np.mean(time_differences)

    return mean_time_difference