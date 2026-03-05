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
    # Convert the Unix timestamp to a datetime object in the target timezone
    target_timezone = pytz.timezone(target_timezone)
    target_datetime = datetime.fromtimestamp(unix_timestamp, target_timezone)

    # Format the datetime object as a string in the target timezone
    return target_datetime.strftime(DATE_FORMAT)