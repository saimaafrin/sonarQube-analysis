from datetime import datetime
import pytz
import numpy as np
def task_func(time_strings, timezone):
    """
    Calculates the average time difference in seconds between each consecutive pair of timestamps in a given list, after converting them to a specified timezone.

    Parameters
    ----------
    time_strings : list of str
        List of timestamps in ISO format.
    timezone : str
        Timezone to convert the timestamps to.

    Returns
    -------
    float
        Mean (average) time difference in seconds between each consecutive pair of timestamps.
    """
    # Convert the timestamps to the specified timezone
    converted_timestamps = [pytz.timezone(timezone).localize(datetime.fromisoformat(ts)) for ts in time_strings]

    # Calculate the time differences between consecutive pairs of timestamps
    time_differences = [abs(converted_timestamps[i] - converted_timestamps[i+1]) for i in range(len(converted_timestamps)-1)]

    # Calculate the mean time difference
    mean_time_diff = np.mean(time_differences)

    # Return the mean time difference
    return mean_time_diff