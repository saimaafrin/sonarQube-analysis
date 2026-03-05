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
    date = parse(date_str, tzinfos={'UTC': pytz.utc})
    date = date.astimezone(pytz.timezone(to_tz))
    year = date.year
    month = date.month
    day = date.day
    hour = date.hour
    minute = date.minute
    second = date.second
    # Calculate the lunar phase
    lunar_phase = 0
    for i in range(len(MOON_PHASES_YEARS)):
        if year >= MOON_PHASES_YEARS[i]:
            lunar_phase = i / len(MOON_PHASES_YEARS)
            break
    # Calculate the moon phase
    moon_phase = (lunar_phase + (day + (hour + (minute + second / 60) / 60) / 24) / 365) % 1
    return moon_phase