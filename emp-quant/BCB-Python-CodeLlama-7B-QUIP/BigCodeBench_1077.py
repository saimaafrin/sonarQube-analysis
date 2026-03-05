
from datetime import datetime
import pytz
import numpy as np

def task_func(time_strings, timezone):
    # Convert the time strings to datetime objects in the specified timezone
    time_objects = [pytz.time_zone(timezone).localize(datetime.strptime(time_string, '%Y-%m-%d %H:%M:%S')) for time_string in time_strings]

    # Calculate the time differences in seconds between consecutive pairs of timestamps
    time_differences = [time_objects[i] - time_objects[i - 1] for i in range(1, len(time_objects))]

    # Calculate the mean time difference in seconds using numpy's mean function
    mean_time_diff = np.mean(time_differences)

    return mean_time_diff