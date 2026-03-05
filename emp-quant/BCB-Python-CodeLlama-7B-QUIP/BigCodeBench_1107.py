
from datetime import datetime
import pytz

# Constants
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

def task_func(unix_timestamp, target_timezone):
    # Convert the timestamp to a datetime object in the target timezone
    target_timezone_dt = datetime.fromtimestamp(unix_timestamp, pytz.timezone(target_timezone))

    # Format the datetime object as a string in the target timezone
    return target_timezone_dt.strftime(DATE_FORMAT)