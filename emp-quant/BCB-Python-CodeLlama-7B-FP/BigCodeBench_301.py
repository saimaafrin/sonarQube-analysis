import pytz
import numpy as np
from dateutil.parser import parse
import math
SOLAR_CYCLE_YEARS = np.array([1986, 1996, 2008, 2019])
def task_func(date_str, from_tz, to_tz):
    """
    Calculate solar activity based on the date and time, taking into account the solar cycle of 11 years.
    The function should output with:
        float: The solar activity between 0 and 1. The value represents the solar activity
        calculated using a cosine function based on the years since the closest solar cycle year.
    """
    date = parse(date_str)
    date = date.astimezone(pytz.timezone(from_tz))
    solar_cycle_year = np.argmin(np.abs(SOLAR_CYCLE_YEARS - date.year))
    solar_cycle_year_start = datetime.datetime(solar_cycle_year, 1, 1, 0, 0, 0, 0, pytz.timezone(from_tz))
    solar_cycle_year_end = datetime.datetime(solar_cycle_year + 11, 1, 1, 0, 0, 0, 0, pytz.timezone(from_tz))
    solar_cycle_year_duration = solar_cycle_year_end - solar_cycle_year_start
    solar_cycle_year_progress = (date - solar_cycle_year_start) / solar_cycle_year_duration
    solar_activity = math.cos(solar_cycle_year_progress * 2 * math.pi)
    return solar_activity