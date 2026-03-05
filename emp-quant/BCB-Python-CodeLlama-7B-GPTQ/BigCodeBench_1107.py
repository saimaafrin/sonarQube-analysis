from datetime import datetime
import pytz
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
def task_func(unix_timestamp, target_timezone):
    """
    Converts a Unix timestamp to a formatted date and time string in a specified timezone.
    :param unix_timestamp: The Unix timestamp to convert.
    :param target_timezone: The target timezone to convert the timestamp to.
    :return: A string representing the date and time in the target timezone, formatted as '%Y-%m-%d %H:%M:%S'.
    """
    # Convert the Unix timestamp to a datetime object
    dt = datetime.fromtimestamp(unix_timestamp)

    # Create a timezone object for the target timezone
    target_tz = pytz.timezone(target_timezone)

    # Convert the datetime object to the target timezone
    target_dt = dt.astimezone(target_tz)

    # Format the target datetime object as a string
    return target_dt.strftime(DATE_FORMAT)