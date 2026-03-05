
import pytz
import numpy as np
from dateutil.parser import parse
import math

MOON_PHASES_YEARS = np.array([1987, 1994, 2001, 2008, 2015, 2022])

def task_func(date_str, from_tz, to_tz):
    # Parse the date string into a datetime object
    date = parse(date_str)
    
    # Convert the datetime object from the from_tz timezone to the to_tz timezone
    from_tz = pytz.timezone(from_tz)
    to_tz = pytz.timezone(to_tz)
    date = date.replace(tzinfo=from_tz).astimezone(to_tz)
    
    # Calculate the number of days since the reference year 1987
    reference_year = 1987
    days_since_reference = (date.year - reference_year) * 365 + date.timetuple().tm_yday
    
    # Calculate the moon phase using the lunar cycle of 7 years
    moon_cycle = 7 * 365
    moon_phase = (days_since_reference % moon_cycle) / moon_cycle
    
    return moon_phase