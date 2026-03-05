from datetime import datetime
import pytz
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
    # Create a datetime object from the Unix timestamp
    dt_object = datetime.fromtimestamp(unix_timestamp)
    
    # Set the target timezone
    target_tz = pytz.timezone(target_timezone)
    
    # Localize the datetime object to the target timezone
    localized_dt = target_tz.localize(dt_object)
    
    # Convert the localized datetime object to the desired format
    formatted_date = localized_dt.strftime(DATE_FORMAT)
    
    return formatted_date