import pytz
import numpy as np
from dateutil.parser import parse
import math
MOON_PHASES_YEARS = np.array([1987, 1994, 2001, 2008, 2015, 2022])
def task_func(date_str, from_tz, to_tz):
    """
    Calculate the moon phase by the date and time taking into account the lunar phase cycle of 7 years. The 
    function uses a constant array `MOON_PHASES_YEARS` to determine the reference years for the moon phases.

    Parameters:
    date_str (str): The date string in "yyyy-mm-dd hh:mm:ss" format.
    from_tz (str): The timezone of the given date string.
    to_tz (str): The timezone to which the given date and time should be converted.

    Returns:
    float: The moon phase between 0 and 1. A value of 0 indicates a new moon and a value of 1 indicates a full moon.

    Requirements:
    - pytz
    - numpy
    - dateutil.parser
    - math

    Example:
    >>> task_func('1970-01-01 00:00:00', 'UTC', 'America/New_York')
    0.9749279121818237
    """
    date = parse(date_str)
    date = date.replace(tzinfo=pytz.timezone(from_tz))
    date = date.astimezone(pytz.timezone(to_tz))
    year = date.year
    month = date.month
    day = date.day
    hour = date.hour
    minute = date.minute
    second = date.second
    phase_year = np.where(MOON_PHASES_YEARS == year)[0][0]
    phase_month = month + (phase_year - 1) * 12
    phase_day = day + (phase_month - 1) * 30.4375
    phase_hour = hour + (phase_day - 1) * 24
    phase_minute = minute + (phase_hour - 1) * 60
    phase_second = second + (phase_minute - 1) * 60
    phase = phase_second / 3600 / 24 / 365.25
    phase = phase % 1
    return phase