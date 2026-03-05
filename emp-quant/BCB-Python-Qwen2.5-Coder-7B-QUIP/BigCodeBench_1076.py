
from datetime import datetime
import pandas as pd
# For Python versions lower than 3.9, use 'pytz' instead of 'zoneinfo'
try:
    from zoneinfo import ZoneInfo
except ImportError:
    from pytz import timezone as ZoneInfo
TIME_FORMAT = "%d/%m/%y %H:%M:%S.%f"

def task_func(time_strings, target_tz):
    # Create a DataFrame to store the results
    result_df = pd.DataFrame(columns=['Original Time', 'Converted Time'])
    
    # Iterate over each time string in the input list
    for time_str in time_strings:
        # Convert the UTC time string to a datetime object
        utc_time = datetime.strptime(time_str, TIME_FORMAT)
        
        # Convert the UTC datetime object to the target timezone
        converted_time = utc_time.astimezone(ZoneInfo(target_tz))
        
        # Append the original and converted times to the DataFrame
        result_df = result_df.append({
            'Original Time': time_str,
            'Converted Time': converted_time.strftime(TIME_FORMAT)
        }, ignore_index=True)
    
    return result_df