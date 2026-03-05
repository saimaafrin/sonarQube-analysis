from datetime import datetime
import pandas as pd
TIME_FORMAT = "%d/%m/%y %H:%M:%S.%f"
def task_func(time_strings, target_tz):
    """
    Convert a list of time strings from UTC to a specified timezone and return a DataFrame.
    The function processes each UTC time string in the given list, converts it to the specified timezone, and stores the results in a DataFrame.
    Note that:
    - The function assumes that the input times are in UTC.
    - The function should output with:
        pandas.DataFrame: A DataFrame with two columns: 'Original Time'
        containing the UTC times and 'Converted Time' containing the times converted to the target timezone.
    """
    # Create a list of datetime objects from the time strings
    time_objects = [datetime.strptime(time_string, TIME_FORMAT) for time_string in time_strings]

    # Create a list of tuples containing the original time and the converted time
    converted_times = [(time_object, time_object.astimezone(ZoneInfo(target_tz))) for time_object in time_objects]

    # Create a DataFrame from the list of tuples
    df = pd.DataFrame(converted_times, columns=['Original Time', 'Converted Time'])

    return df
time_strings = ['01/01/2022 12:00:00.000', '01/01/2022 13:00:00.000', '01/01/2022 14:00:00.000']
target_tz = 'Europe/Paris'