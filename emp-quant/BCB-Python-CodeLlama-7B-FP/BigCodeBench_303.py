import pytz
import numpy as np
from dateutil.parser import parse
import math
MOON_PHASES_YEARS = np.array([1987, 1994, 2001, 2008, 2015, 2022])
def task_func(date_str, from_tz, to_tz):
    """
    Calculate the moon phase by the date and time taking into account the lunar phase cycle of 7 years.
    The function uses a constant array `MOON_PHASES_YEARS` to determine the reference years for the moon phases.
    The function should output with:
        float: The moon phase between 0 and 1. A value of 0 indicates a new moon and a value of 1 indicates a full moon.
    """
    date = parse(date_str)
    date = date.astimezone(pytz.timezone(from_tz))
    year = date.year
    month = date.month
    day = date.day
    hour = date.hour
    minute = date.minute
    second = date.second
    moon_phase_year = np.interp(year, MOON_PHASES_YEARS, np.arange(len(MOON_PHASES_YEARS)))
    moon_phase_month = np.interp(month, np.arange(1, 13), np.arange(12))
    moon_phase_day = np.interp(day, np.arange(1, 32), np.arange(31))
    moon_phase_hour = np.interp(hour, np.arange(0, 24), np.arange(24))
    moon_phase_minute = np.interp(minute, np.arange(0, 60), np.arange(60))
    moon_phase_second = np.interp(second, np.arange(0, 60), np.arange(60))
    moon_phase = (moon_phase_year + moon_phase_month + moon_phase_day + moon_phase_hour + moon_phase_minute + moon_phase_second) / 60
    return moon_phase