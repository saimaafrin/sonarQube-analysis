
from datetime import datetime
import pytz

# Constants
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

def task_func(unix_timestamp, target_timezone):
    """
    Converts a Unix timestamp to a formatted date and time string in a specified timezone.
    
    Args:
    unix_timestamp (int): The Unix timestamp to convert.
    target_timezone (str): The target timezone in the format 'Area/City'.
    
    Returns:
    str: A string representing the date and time in the target timezone, formatted as '%Y-%m-%d %H:%M:%S'.
    """
    # Convert the Unix timestamp to a datetime object in UTC
    utc_time = datetime.fromtimestamp(unix_timestamp, pytz.utc)
    
    # Set the target timezone
    target_tz = pytz.timezone(target_timezone)
    
    # Convert the UTC datetime to the target timezone
    target_time = utc_time.astimezone(target_tz)
    
    # Format the datetime object to the specified format
    formatted_time = target_time.strftime(DATE_FORMAT)
    
    return formatted_time