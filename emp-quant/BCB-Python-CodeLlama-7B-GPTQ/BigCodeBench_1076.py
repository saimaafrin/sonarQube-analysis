from datetime import datetime
import pandas as pd
TIME_FORMAT = "%d/%m/%y %H:%M:%S.%f"
def task_func(time_strings, target_tz):
    """
    Convert a list of time strings from UTC to a specified timezone and return a DataFrame.
    The function processes each UTC time string in the given list, converts it to the specified timezone, and stores the results in a DataFrame.
    """
    # Create a list to store the converted times
    converted_times = []

    # Iterate over the time strings in the input list
    for time_string in time_strings:
        # Convert the time string to a datetime object
        utc_time = datetime.strptime(time_string, TIME_FORMAT)

        # Convert the UTC time to the target timezone
        target_time = utc_time.astimezone(ZoneInfo(target_tz))

        # Add the converted time to the list
        converted_times.append(target_time)

    # Create a DataFrame with the original and converted times
    df = pd.DataFrame({
        "Original Time": time_strings,
        "Converted Time": converted_times
    })

    return df
time_strings = ["01/01/2020 12:00:00.000", "01/01/2020 13:00:00.000", "01/01/2020 14:00:00.000"]
target_tz = "Europe/London"