
import pytz
import numpy as np
from dateutil.parser import parse
import math

MOON_PHASES_YEARS = np.array([1987, 1994, 2001, 2008, 2015, 2022])

def task_func(date_str, from_tz, to_tz):
    # Parse the input date string
    date = parse(date_str)
    
    # Convert the date to the target timezone
    from_tz = pytz.timezone(from_tz)
    to_tz = pytz.timezone(to_tz)
    date = date.replace(tzinfo=from_tz).astimezone(to_tz)
    
    # Calculate the year and day of the year
    year = date.year
    day_of_year = date.timetuple().tm_yday
    
    # Calculate the moon phase
    # The moon phase cycle is approximately 29.53 days
    # We use the year and day of the year to determine the moon phase
    # The formula is based on the assumption that the moon phase is 0 on the first day of the year
    moon_phase = (day_of_year - 1) / 29.53
    
    # Normalize the moon phase to be between 0 and 1
    moon_phase = moon_phase % 1
    
    # Adjust the moon phase based on the reference years
    # The moon phase is the same every 7 years
    # We use the reference years to determine the moon phase
    reference_year_index = np.where(MOON_PHASES_YEARS == year)[0]
    if reference_year_index.size > 0:
        reference_year_index = reference_year_index[0]
        moon_phase = MOON_PHASES_YEARS[reference_year_index] + moon_phase
    
    # Return the moon phase
    return moon_phase