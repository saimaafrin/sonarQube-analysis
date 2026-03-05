
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
    # Parse the given date string
    given_date = parse(date_str)

    # Get the current time
    current_time = datetime.now()

    # Calculate the total number of seconds elapsed since the given date
    total_seconds = (current_time - given_date).total_seconds()

    # Initialize the number of leap seconds to 0
    leap_seconds = 0

    # Iterate over the years when leap seconds were added
    for year in LEAP_SECONDS:
        # Check if the given date is in the same year as the leap second
        if given_date.year == year:
            # Increment the number of leap seconds
            leap_seconds += 1

    # Return the total number of elapsed seconds, including leap seconds
    return total_seconds + leap_seconds