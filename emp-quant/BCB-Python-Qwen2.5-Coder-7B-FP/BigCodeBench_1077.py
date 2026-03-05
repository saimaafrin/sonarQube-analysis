from datetime import datetime
import pytz
import numpy as np
def task_func(time_strings, timezone):
    # Convert the timezone string to a pytz timezone object
    tz = pytz.timezone(timezone)
    
    # Convert each time string to a datetime object in the specified timezone
    dt_objects = [datetime.strptime(ts, '%Y-%m-%d %H:%M:%S').replace(tzinfo=pytz.utc).astimezone(tz) for ts in time_strings]
    
    # Calculate the absolute time difference in seconds between each consecutive pair of timestamps
    time_differences = [abs((dt_objects[i] - dt_objects[i-1]).total_seconds()) for i in range(1, len(dt_objects))]
    
    # If there are less than two timestamps, return 0.0
    if len(time_differences) < 1:
        return 0.0
    
    # Calculate and return the mean (average) time difference in seconds
    return np.mean(time_differences)