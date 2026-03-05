
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
    date = parse(date_str)
    current_time = datetime.now()
    elapsed_time = current_time - date
    leap_seconds = np.sum(np.where(LEAP_SECONDS >= date.year, 1, 0))
    return elapsed_time.total_seconds + leap_seconds