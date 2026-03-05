from datetime import datetime
import pytz
from dateutil.parser import parse
def task_func(date_str, tz_str):
    """
    Determine the time in seconds until the next turn of the year in a certain time zone from a given date string.
    :param date_str: A string representing a date in the format "YYYY-MM-DD HH:MM:SS"
    :param tz_str: A string representing a time zone in the format "UTC+/-HH:MM"
    :return: The time in seconds until the next New Year in the specified timezone
    """
    # Parse the date and time strings
    date_obj = parse(date_str)
    tz_obj = pytz.timezone(tz_str)

    # Convert the date and time to the specified time zone
    tz_date_obj = tz_obj.localize(date_obj)

    # Calculate the time until the next New Year in the specified time zone
    next_year_date = datetime(tz_date_obj.year + 1, 1, 1, 0, 0, 0, 0, tz_obj)
    time_until_next_year = next_year_date - tz_date_obj

    # Return the time in seconds
    return time_until_next_year.total_seconds()
date_str = "2022-01-01 00:00:00"
tz_str = "UTC+00:00"