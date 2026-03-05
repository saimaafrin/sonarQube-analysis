from datetime import datetime
import pandas as pd
TIME_FORMAT = "%d/%m/%y %H:%M:%S.%f"
def task_func(time_strings, target_tz):
    # Convert the list of time strings to a list of datetime objects in UTC
    utc_times = [datetime.strptime(time_str, TIME_FORMAT) for time_str in time_strings]
    
    # Convert each UTC datetime to the specified timezone
    converted_times = [utc_time.replace(tzinfo=ZoneInfo('UTC')).astimezone(ZoneInfo(target_tz)) for utc_time in utc_times]
    
    # Create a DataFrame with the original and converted times
    result_df = pd.DataFrame({
        'Original Time': [time.strftime(TIME_FORMAT) for time in utc_times],
        'Converted Time': [time.strftime(TIME_FORMAT) for time in converted_times]
    })
    
    return result_df