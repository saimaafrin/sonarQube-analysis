
from datetime import datetime
import pandas as pd
# For Python versions lower than 3.9, use 'pytz' instead of 'zoneinfo'
try:
    from zoneinfo import ZoneInfo
except ImportError:
    from pytz import timezone as ZoneInfo
TIME_FORMAT = "%d/%m/%y %H:%M:%S.%f"
def task_func(time_strings, target_tz):
    # Create a list of datetime objects from the time strings
    datetime_list = [datetime.strptime(time_string, TIME_FORMAT) for time_string in time_strings]
    # Create a list of timezone objects from the target timezone
    target_tz_list = [ZoneInfo(target_tz) for _ in range(len(datetime_list))]
    # Convert the datetime objects to the target timezone
    converted_datetime_list = [datetime.astimezone(target_tz) for datetime, target_tz in zip(datetime_list, target_tz_list)]
    # Create a DataFrame with the original and converted times
    df = pd.DataFrame({
        "Original Time": datetime_list,
        "Converted Time": converted_datetime_list
    })
    return df