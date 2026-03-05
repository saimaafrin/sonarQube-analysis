import pytz
import numpy as np
from dateutil.parser import parse
import math
MOON_PHASES_YEARS = np.array([1987, 1994, 2001, 2008, 2015, 2022])
def task_func(date_str, from_tz, to_tz):
    # Parse the input date string into a datetime object
    date = parse(date_str)
    
    # Convert the datetime object from the from_tz timezone to the to_tz timezone
    date = date.replace(tzinfo=pytz.timezone(from_tz)).astimezone(pytz.timezone(to_tz))
    
    # Calculate the year of the input date
    year = date.year
    
    # Calculate the difference between the input year and the reference years
    diff = year - MOON_PHASES_YEARS
    
    # Calculate the moon phase by taking the absolute value of the difference and dividing by the length of the MOON_PHASES_YEARS array
    moon_phase = abs(diff) / len(MOON_PHASES_YEARS)
    
    # Return the moon phase as a float between 0 and 1
    return moon_phase