from datetime import datetime
import pandas as pd
TIME_FORMAT = "%d/%m/%y %H:%M:%S.%f"
def task_func(time_strings, target_tz):
    # Create an empty list to store the converted times
    converted_times = []
    
    # Iterate over each time string in the input list
    for time_str in time_strings:
        # Convert the time string to a datetime object in UTC
        utc_time = datetime.strptime(time_str, TIME_FORMAT)
        
        # Convert the UTC datetime object to the target timezone
        target_tz_info = ZoneInfo(target_tz)
        converted_time = utc_time.astimezone(target_tz_info)
        
        # Append the converted time to the list
        converted_times.append(converted_time)
    
    # Create a DataFrame with the original and converted times
    df = pd.DataFrame({
        'Original Time': time_strings,
        'Converted Time': converted_times
    })
    
    return df