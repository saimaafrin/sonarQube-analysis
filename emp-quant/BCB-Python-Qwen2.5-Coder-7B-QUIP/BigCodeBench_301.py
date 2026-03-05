
import pytz
import numpy as np
from dateutil.parser import parse
import math
SOLAR_CYCLE_YEARS = np.array([1986, 1996, 2008, 2019])

def task_func(date_str, from_tz, to_tz):
    # Parse the input date string and convert it to a datetime object
    date = parse(date_str)
    
    # Convert the datetime object to the specified timezone
    date = pytz.timezone(from_tz).localize(date, is_dst=None)
    date = date.astimezone(pytz.timezone(to_tz))
    
    # Calculate the year from the datetime object
    year = date.year
    
    # Find the closest solar cycle year
    closest_year = SOLAR_CYCLE_YEARS[np.argmin(np.abs(SOLAR_CYCLE_YEARS - year))]
    
    # Calculate the solar activity using a cosine function
    solar_activity = 0.5 * (1 + math.cos(2 * math.pi * (year - closest_year) / 11))
    
    return solar_activity