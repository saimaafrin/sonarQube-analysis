
from datetime import datetime
import numpy as np
from dateutil.parser import parse
LEAP_SECONDS = np.array(
    [
        1972,
        1973,
        1974,
        1975,
        1976,
        1977,
        1978,
        1979,
        1980,
        1981,
        1982,
        1983,
        1985,
        1988,
        1990,
        1993,
        1994,
        1997,
        1999,
        2006,
        2009,
        2012,
        2015,
        2016,
        2020,
    ]
)
def task_func(date_str):
    # Parse the input date string into a datetime object
    given_date = parse(date_str)
    
    # Get the current datetime
    current_date = datetime.now()
    
    # Calculate the difference in days between the current date and the given date
    delta = current_date - given_date
    
    # Calculate the total number of seconds, including leap seconds
    total_seconds = delta.days * 24 * 60 * 60 + delta.seconds
    
    # Add leap seconds for the years between the given date and the current date
    leap_seconds = np.sum((given_date.year < LEAP_SECONDS) & (LEAP_SECONDS <= current_date.year))
    
    # Return the total number of seconds including leap seconds
    return total_seconds + leap_seconds