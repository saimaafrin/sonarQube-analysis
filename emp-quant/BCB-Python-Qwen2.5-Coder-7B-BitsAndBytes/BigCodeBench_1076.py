
from datetime import datetime
import pandas as pd
# For Python versions lower than 3.9, use 'pytz' instead of 'zoneinfo'
try:
    from zoneinfo import ZoneInfo
except ImportError:
    from pytz import timezone as ZoneInfo

TIME_FORMAT = "%d/%m/%y %H:%M:%S.%f"

def task_func(time_strings, target_tz):
    # Create an empty list to store the results
    results = []
    
    # Iterate over each time string in the input list
    for time_str in time_strings:
        # Convert the time string to a datetime object assuming UTC
        utc_time = datetime.strptime(time_str, TIME_FORMAT)
        
        # Convert the UTC time to the target timezone
        target_timezone = ZoneInfo(target_tz)
        converted_time = utc_time.replace(tzinfo=ZoneInfo('UTC')).astimezone(target_timezone)
        
        # Append the original and converted times to the results list
        results.append({'Original Time': time_str, 'Converted Time': converted_time.strftime(TIME_FORMAT)})
    
    # Create a DataFrame from the results list
    df = pd.DataFrame(results)
    
    return df