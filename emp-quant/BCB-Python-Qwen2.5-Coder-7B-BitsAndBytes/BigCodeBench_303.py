
import pytz
import numpy as np
from dateutil.parser import parse
import math

MOON_PHASES_YEARS = np.array([1987, 1994, 2001, 2008, 2015, 2022])

def task_func(date_str, from_tz, to_tz):
    # Parse the input date string
    dt = parse(date_str)
    
    # Convert the timezone of the input date
    from_tz_obj = pytz.timezone(from_tz)
    to_tz_obj = pytz.timezone(to_tz)
    dt_converted = dt.replace(tzinfo=from_tz_obj).astimezone(to_tz_obj)
    
    # Calculate the year difference from the reference years
    year_diff = dt_converted.year - MOON_PHASES_YEARS[0]
    
    # Calculate the moon phase based on the year difference
    moon_phase = (year_diff % 7) / 7
    
    return moon_phase