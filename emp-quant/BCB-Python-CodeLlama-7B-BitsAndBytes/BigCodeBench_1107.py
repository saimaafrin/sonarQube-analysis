
from datetime import datetime
import pytz

# Constants
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

def task_func(unix_timestamp, target_timezone):
    # Convert the Unix timestamp to a datetime object
    dt = datetime.fromtimestamp(unix_timestamp)

    # Convert the datetime object to the target timezone
    target_tz = pytz.timezone(target_timezone)
    dt_target_tz = dt.astimezone(target_tz)

    # Format the datetime object in the target timezone
    formatted_dt = dt_target_tz.strftime(DATE_FORMAT)

    return formatted_dt