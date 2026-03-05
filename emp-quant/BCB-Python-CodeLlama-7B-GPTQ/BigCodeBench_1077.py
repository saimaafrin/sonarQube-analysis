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
    converted_timestamps = [pytz.timezone(timezone).localize(datetime.strptime(time_string, '%Y-%m-%d %H:%M:%S')) for time_string in time_strings]

    # Calculate the absolute time difference in seconds between each consecutive pair of timestamps
    time_differences = [abs(converted_timestamps[i] - converted_timestamps[i + 1]).total_seconds() for i in range(len(converted_timestamps) - 1)]

    # Calculate the mean time difference using numpy's mean function
    mean_time_difference = np.mean(time_differences)

    # Return the mean time difference
    return mean_time_difference
time_strings = ['2022-01-01 00:00:00', '2022-01-01 00:00:10', '2022-01-01 00:00:20', '2022-01-01 00:00:30']
timezone = 'UTC'