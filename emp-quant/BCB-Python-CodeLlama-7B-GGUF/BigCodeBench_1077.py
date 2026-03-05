
from datetime import datetime
import pytz
import numpy as np

def task_func(time_strings, timezone):
    # Convert the timestamps to the specified timezone
    time_strings = [pytz.timezone(timezone).localize(datetime.strptime(time_string, '%Y-%m-%d %H:%M:%S')) for time_string in time_strings]

    # Calculate the absolute time difference in seconds between each consecutive pair of timestamps
    time_differences = [abs(time_strings[i] - time_strings[i-1]).total_seconds() for i in range(1, len(time_strings))]

    # Calculate the mean time difference in seconds
    mean_time_difference = np.mean(time_differences)

    return mean_time_difference