from datetime import datetime
import pytz
import numpy as np
def task_func(time_strings, timezone):
    """
    Calculates the average time difference in seconds between each consecutive pair of timestamps
    in a given list, after converting them to a specified timezone.
    
    :param time_strings: List of strings representing timestamps in ISO format.
    :param timezone: String representing the target timezone.
    :return: float: The mean (average) time difference in seconds between each consecutive pair of timestamps.
    """
    # Convert the list of time strings to datetime objects in the specified timezone
    target_tz = pytz.timezone(timezone)
    timestamps = [datetime.fromisoformat(ts).astimezone(target_tz) for ts in time_strings]
    
    # Calculate the time differences in seconds between consecutive timestamps
    time_differences = [timestamps[i+1] - timestamps[i] for i in range(len(timestamps)-1)]
    time_differences_seconds = [diff.total_seconds() for diff in time_differences]
    
    # Calculate the mean time difference
    if len(time_differences_seconds) == 0:
        return 0.0
    mean_time_difference = np.mean(time_differences_seconds)
    
    return mean_time_difference
time_strings = ["2023-04-01T12:00:00Z", "2023-04-01T12:05:00Z", "2023-04-01T12:10:00Z"]
timezone = "America/New_York"