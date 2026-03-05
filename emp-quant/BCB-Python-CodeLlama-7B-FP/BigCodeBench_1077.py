from datetime import datetime
import pytz
import numpy as np
def task_func(time_strings, timezone):
    """
    Calculates the average time difference in seconds between each consecutive pair of timestamps in a given list, after converting them to a specified timezone.

    Parameters
    ----------
    time_strings : list of str
        List of timestamps in string format.
    timezone : str
        Timezone to convert the timestamps to.

    Returns
    -------
    float
        Mean (average) time difference in seconds between each consecutive pair of timestamps.
    """
    # Convert the timestamps to the specified timezone
    converted_timestamps = [pytz.timezone(timezone).localize(datetime.strptime(ts, '%Y-%m-%d %H:%M:%S')) for ts in time_strings]

    # Calculate the absolute time difference in seconds between each consecutive pair of timestamps
    time_differences = [abs(converted_timestamps[i] - converted_timestamps[i + 1]).total_seconds() for i in range(len(converted_timestamps) - 1)]

    # Calculate the mean time difference using numpy's mean function
    mean_time_difference = np.mean(time_differences)

    return mean_time_difference