from datetime import datetime
import pytz
from dateutil.parser import parse
def task_func(date_str, tz_str):
    """
    Determine the time in seconds until the next turn of the year in a certain time zone from a given date string.
    :param date_str: A date string in the format 'YYYY-MM-DD HH:MM:SS'.
    :param tz_str: A time zone string in the format 'UTC+/-HH:MM'.
    :return: The time in seconds until the next New Year in the specified timezone.
    """
    # Parse the date string and time zone string
    date = parse(date_str)
    tz = pytz.timezone(tz_str)

    # Convert the date to the specified time zone
    date_tz = date.astimezone(tz)

    # Calculate the time in seconds until the next New Year
    next_year = date_tz.replace(year=date_tz.year + 1)
    delta = next_year - date_tz

    # Return the time in seconds
    return delta.total_seconds()