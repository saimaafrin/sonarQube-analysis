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
    date_obj = parse(date_str)
    tz_obj = pytz.timezone(tz_str)

    # Convert the date object to the specified time zone
    tz_date_obj = date_obj.astimezone(tz_obj)

    # Calculate the time in seconds until the next New Year
    next_new_year = tz_date_obj.replace(year=tz_date_obj.year + 1) - tz_date_obj

    # Return the time in seconds
    return next_new_year.total_seconds()