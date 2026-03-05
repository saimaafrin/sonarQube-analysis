
import pytz
import numpy as np
from dateutil.parser import parse
import math

SOLAR_CYCLE_YEARS = np.array([1986, 1996, 2008, 2019])

def task_func(date_str, from_tz, to_tz):
    # Parse the date string into a datetime object
    dt = parse(date_str)
    
    # Convert the datetime object from the from_tz timezone to UTC
    dt_utc = dt.replace(tzinfo=pytz.timezone(from_tz)).astimezone(pytz.utc)
    
    # Convert the datetime object from UTC to the to_tz timezone
    dt_to_tz = dt_utc.astimezone(pytz.timezone(to_tz))
    
    # Extract the year from the datetime object
    year = dt_to_tz.year
    
    # Find the closest solar cycle year
    closest_year = min(SOLAR_CYCLE_YEARS, key=lambda x: abs(x - year))
    
    # Calculate the number of years since the closest solar cycle year
    years_since_cycle = year - closest_year
    
    # Calculate the solar activity using a cosine function
    solar_activity = 0.5 * (1 + math.cos(2 * math.pi * years_since_cycle / 11))
    
    return solar_activity