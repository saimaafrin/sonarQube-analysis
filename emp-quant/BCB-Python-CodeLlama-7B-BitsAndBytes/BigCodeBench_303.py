
import pytz
import numpy as np
from dateutil.parser import parse
import math

MOON_PHASES_YEARS = np.array([1987, 1994, 2001, 2008, 2015, 2022])

def task_func(date_str, from_tz, to_tz):
    # Parse the date string and convert it to a datetime object
    date = parse(date_str)
    date = date.replace(tzinfo=pytz.timezone(from_tz))

    # Calculate the number of days since the reference year
    days_since_ref = (date - MOON_PHASES_YEARS[0]).days

    # Calculate the moon phase based on the number of days since the reference year
    moon_phase = math.fmod(days_since_ref, 7) / 7

    # Convert the moon phase to a value between 0 and 1
    moon_phase = moon_phase * 2 - 1

    return moon_phase