
from datetime import datetime
import pytz

# Constants
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

def task_func(unix_timestamp, target_timezone):
    # Convert Unix timestamp to datetime object
    dt = datetime.fromtimestamp(unix_timestamp)

    # Convert to target timezone
    tz = pytz.timezone(target_timezone)
    dt_tz = dt.astimezone(tz)

    # Format date and time string
    return dt_tz.strftime(DATE_FORMAT)