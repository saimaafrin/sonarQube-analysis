
from datetime import datetime
import pytz
import numpy as np

def task_func(time_strings, timezone):
    if len(time_strings) < 2:
        return 0.0
    
    # Convert the timezone string to a pytz timezone object
    tz = pytz.timezone(timezone)
    
    # Convert each timestamp string to a datetime object in the specified timezone
    timestamps = [datetime.strptime(ts, '%Y-%m-%d %H:%M:%S').replace(tzinfo=pytz.utc).astimezone(tz) for ts in time_strings]
    
    # Calculate the absolute time difference in seconds between each consecutive pair of timestamps
    time_differences = [abs((timestamps[i] - timestamps[i-1]).total_seconds()) for i in range(1, len(timestamps))]
    
    # Calculate the mean (average) time difference
    mean_time_difference = np.mean(time_differences)
    
    return mean_time_difference