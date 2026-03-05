
import pytz
import numpy as np
from dateutil.parser import parse
import math
MOON_PHASES_YEARS = np.array([1987, 1994, 2001, 2008, 2015, 2022])

def task_func(date_str, from_tz, to_tz):
    # Parse the input date string and convert it to a datetime object
    date = parse(date_str)
    
    # Set the time zone for the input date
    from_tz = pytz.timezone(from_tz)
    to_tz = pytz.timezone(to_tz)
    date = from_tz.localize(date)
    
    # Convert the date to the target time zone
    date = date.astimezone(to_tz)
    
    # Calculate the year of the input date
    year = date.year
    
    # Calculate the index of the reference year
    index = np.where(MOON_PHASES_YEARS == year)[0]
    
    # If the year is not in the reference years, use the closest reference year
    if len(index) == 0:
        index = np.where(MOON_PHASES_YEARS > year)[0]
        if len(index) == 0:
            index = np.where(MOON_PHASES_YEARS < year)[0]
            if len(index) == 0:
                raise ValueError("Year not found in reference years")
    
    # Calculate the moon phase
    moon_phase = (year - MOON_PHASES_YEARS[index[0]]) / (MOON_PHASES_YEARS[index[0]] - MOON_PHASES_YEARS[index[0] - 1]) if index[0] > 0 else 0
    
    # Return the moon phase between 0 and 1
    return moon_phase