
from datetime import datetime
import pytz

# Constants
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

def task_func(unix_timestamp, target_timezone):
    """
    Converts a Unix timestamp to a formatted date and time string in a specified timezone.
    
    Parameters:
    unix_timestamp (int): The Unix timestamp to convert.
    target_timezone (str): The target timezone in pytz format (e.g., 'America/New_York').
    
    Returns:
    str: A string representing the date and time in the target timezone, formatted as '%Y-%m-%d %H:%M:%S'.
    """
    # Convert the Unix timestamp to a datetime object in UTC
    utc_time = datetime.fromtimestamp(unix_timestamp, pytz.utc)
    
    # Set the target timezone
    target_tz = pytz.timezone(target_timezone)
    
    # Localize the UTC time to the target timezone
    localized_time = utc_time.astimezone(target_tz)
    
    # Format the localized time as a string
    formatted_time = localized_time.strftime(DATE_FORMAT)
    
    return formatted_time