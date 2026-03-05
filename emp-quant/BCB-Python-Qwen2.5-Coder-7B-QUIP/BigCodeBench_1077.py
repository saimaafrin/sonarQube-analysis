
from datetime import datetime
import pytz
import numpy as np

def task_func(time_strings, timezone):
    # Convert each timestamp to the specified timezone
    timezone = pytz.timezone(timezone)
    timestamps = [datetime.strptime(ts, '%Y-%m-%d %H:%M:%S').replace(tzinfo=pytz.utc).astimezone(timezone) for ts in time_strings]
    
    # Calculate the absolute time difference in seconds between each consecutive pair of timestamps
    time_differences = [abs((timestamps[i] - timestamps[i-1]).total_seconds()) for i in range(1, len(timestamps))]
    
    # If there are less than two timestamps, return 0.0
    if len(time_strings) < 2:
        return 0.0
    
    # Calculate and return the mean time difference
    return np.mean(time_differences)