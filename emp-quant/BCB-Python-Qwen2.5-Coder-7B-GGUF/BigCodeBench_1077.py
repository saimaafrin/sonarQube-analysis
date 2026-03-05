
from datetime import datetime
import pytz
import numpy as np

def task_func(time_strings, timezone):
    if len(time_strings) < 2:
        return 0.0
    
    # Convert each timestamp to the specified timezone
    timezone = pytz.timezone(timezone)
    converted_times = [datetime.strptime(ts, '%Y-%m-%d %H:%M:%S').replace(tzinfo=pytz.utc).astimezone(timezone) for ts in time_strings]
    
    # Calculate the absolute time difference in seconds between each consecutive pair of timestamps
    time_differences = [abs((converted_times[i] - converted_times[i-1]).total_seconds()) for i in range(1, len(converted_times))]
    
    # Return the mean (average) time difference
    return np.mean(time_differences)