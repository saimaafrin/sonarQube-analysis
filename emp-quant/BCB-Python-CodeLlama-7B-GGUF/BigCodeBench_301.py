
import pytz
import numpy as np
from dateutil.parser import parse
import math

SOLAR_CYCLE_YEARS = np.array([1986, 1996, 2008, 2019])

def task_func(date_str, from_tz, to_tz):
    # Parse the date string and convert it to a datetime object
    date = parse(date_str)
    date = date.replace(tzinfo=pytz.timezone(from_tz))
    date = date.astimezone(pytz.timezone(to_tz))

    # Calculate the number of years since the closest solar cycle year
    years_since_cycle = (date.year - SOLAR_CYCLE_YEARS[0]) % 11

    # Calculate the solar activity using a cosine function
    solar_activity = math.cos(math.radians(years_since_cycle * 360))

    # Return the solar activity between 0 and 1
    return solar_activity