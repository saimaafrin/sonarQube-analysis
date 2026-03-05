
from datetime import datetime
import pytz

# Constants
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

def task_func(unix_timestamp, target_timezone):
    # Convert the Unix timestamp to a datetime object in UTC
    utc_time = datetime.fromtimestamp(unix_timestamp, pytz.utc)
    
    # Set the target timezone
    target_tz = pytz.timezone(target_timezone)
    
    # Convert the UTC time to the target timezone
    target_time = utc_time.astimezone(target_tz)
    
    # Format the target time as a string
    formatted_time = target_time.strftime(DATE_FORMAT)
    
    return formatted_time