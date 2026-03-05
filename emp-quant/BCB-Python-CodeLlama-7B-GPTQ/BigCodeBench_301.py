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
    solar_cycle_year_days = (date.year - solar_cycle_year) * 365.25
    solar_cycle_year_cos = math.cos(solar_cycle_year_days / 11)
    solar_activity = solar_cycle_year_cos * 0.5 + 0.5
    return solar_activity