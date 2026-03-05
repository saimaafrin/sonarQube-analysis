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
    """
    Calculate the total number of seconds elapsed from a given date until the current time, including any leap seconds that occurred in this period.
    """
    date = parse(date_str)
    current_time = datetime.now()
    total_seconds = (current_time - date).total_seconds()
    leap_seconds = 0
    for year in LEAP_SECONDS:
        if year >= date.year and year <= current_time.year:
            leap_seconds += 1
    return total_seconds + leap_seconds