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
    # Parse the date and time
    date = parse(date_str)
    date = date.astimezone(pytz.timezone(from_tz))

    # Calculate the years since the closest solar cycle year
    years_since_cycle = (date.year - SOLAR_CYCLE_YEARS[0]) % 11

    # Calculate the solar activity using a cosine function
    solar_activity = math.cos(years_since_cycle * math.pi / 5.5)

    # Return the solar activity
    return solar_activity