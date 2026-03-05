from datetime import datetime
import pytz
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
def task_func(unix_timestamp, target_timezone):
    """
    Converts a Unix timestamp to a formatted date and time string in a specified timezone.

    Args:
        unix_timestamp (int): The Unix timestamp to convert.
        target_timezone (str): The target timezone to convert the timestamp to.

    Returns:
        str: A string representing the date and time in the target timezone, formatted as '%Y-%m-%d %H:%M:%S'.
    """
    # Convert the Unix timestamp to a datetime object
    dt = datetime.fromtimestamp(unix_timestamp)

    # Convert the datetime object to the target timezone
    tz = pytz.timezone(target_timezone)
    dt_tz = tz.localize(dt)

    # Format the datetime object as a string
    return dt_tz.strftime(DATE_FORMAT)