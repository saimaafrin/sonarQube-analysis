
import pytz
import numpy as np
from dateutil.parser import parse
import math

SOLAR_CYCLE_YEARS = np.array([1986, 1996, 2008, 2019])

def task_func(date_str, from_tz, to_tz):
    # Parse the input date string to a datetime object
    dt = parse(date_str)
    
    # Convert the datetime object from the source timezone to UTC
    from_tz_obj = pytz.timezone(from_tz)
    to_tz_obj = pytz.timezone(to_tz)
    dt_utc = dt.replace(tzinfo=from_tz_obj).astimezone(pytz.utc)
    
    # Extract the year from the UTC datetime object
    year = dt_utc.year
    
    # Find the closest solar cycle year
    closest_year = min(SOLAR_CYCLE_YEARS, key=lambda x: abs(x - year))
    
    # Calculate the number of years since the closest solar cycle year
    years_since_cycle = year - closest_year
    
    # Normalize the years since the cycle to a range of 0 to 1
    normalized_years = years_since_cycle / (max(SOLAR_CYCLE_YEARS) - min(SOLAR_CYCLE_YEARS))
    
    # Calculate the solar activity using a cosine function
    solar_activity = 0.5 * (1 + math.cos(2 * math.pi * normalized_years))
    
    return solar_activity