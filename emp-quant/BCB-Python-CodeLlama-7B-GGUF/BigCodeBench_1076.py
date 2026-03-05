
from datetime import datetime
import pandas as pd
# For Python versions lower than 3.9, use 'pytz' instead of 'zoneinfo'
try:
    from zoneinfo import ZoneInfo
except ImportError:
    from pytz import timezone as ZoneInfo

TIME_FORMAT = "%d/%m/%y %H:%M:%S.%f"

def task_func(time_strings, target_tz):
    # Convert the time strings to datetime objects
    utc_times = [datetime.strptime(time_string, TIME_FORMAT) for time_string in time_strings]

    # Convert the UTC times to the target timezone
    target_times = [utc_time.astimezone(ZoneInfo(target_tz)) for utc_time in utc_times]

    # Create a DataFrame with the original and converted times
    df = pd.DataFrame({'Original Time': utc_times, 'Converted Time': target_times})

    return df