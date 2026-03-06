import pytz
import numpy as np
from dateutil.parser import parse
import math
SOLAR_CYCLE_YEARS = np.array([1986, 1996, 2008, 2019])
def task_func(date_str, from_tz, to_tz):
    """
    Calculate solar activity based on the date and time, taking into account the solar cycle of 11 years.

    Parameters:
    date_str (str): The date string in "yyyy-mm-dd hh:mm:ss" format.
    from_tz (str): The timezone of the given date string.
    to_tz (str): The timezone to which the given date and time should be converted.

    Returns:
    float: The solar activity between 0 and 1. The value represents the solar activity 
           calculated using a cosine function based on the years since the closest solar cycle year.

    Requirements:
    - pytz
    - numpy
    - dateutil.parser
    - math

    Example:
    >>> task_func('1970-01-01 00:00:00', 'UTC', 'America/New_York')
    0.14231483827328487
    >>> task_func('1990-01-01 00:00:00', 'UTC', 'America/New_York')
    0.6548607339452851
    """
    date = parse(date_str)
    date = date.astimezone(pytz.timezone(from_tz))
    date = date.astimezone(pytz.timezone(to_tz))
    year = date.year
    solar_cycle_year = SOLAR_CYCLE_YEARS[np.argmin(np.abs(SOLAR_CYCLE_YEARS - year))]
    solar_cycle_year_start = parse(str(solar_cycle_year) + '-01-01 00:00:00')
    solar_cycle_year_start = solar_cycle_year_start.astimezone(pytz.timezone(from_tz))
    solar_cycle_year_start = solar_cycle_year_start.astimezone(pytz.timezone(to_tz))
    solar_cycle_year_end = parse(str(solar_cycle_year + 11) + '-01-01 00:00:00')
    solar_cycle_year_end = solar_cycle_year_end.astimezone(pytz.timezone(from_tz))
    solar_cycle_year_end = solar_cycle_year_end.astimezone(pytz.timezone(to_tz))
    solar_cycle_year_duration = solar_cycle_year_end - solar_cycle_year_start
    solar_cycle_year_duration_in_seconds = solar_cycle_year_duration.total_seconds()
    solar_cycle_year_duration_in_days = solar_cycle_year_duration_in_seconds / (24 * 60 * 60)
    solar_cycle_year_duration_in_years = solar_cycle_year_duration_in_days / 365.25
    solar_cycle_year_duration_in_years_in_seconds = solar_cycle_year_duration_in_years * 365.25 * 24 * 60 * 60
    solar_cycle_year_duration_in_years_in_days = solar_cycle_year_duration_in_years * 365.25
    solar_cycle_year_duration_in_years_in_hours = solar_cycle_year_duration_in_years * 24
    solar_cycle_year_duration_in_years_in_minutes = solar_cycle_year_duration_in_years * 24 * 60
    solar_cycle_year_duration_in_years_in_seconds = solar_cycle_year_duration_in_years * 24 * 60 * 60
    solar_cycle_year_duration_in_years_in_milliseconds = solar_cycle_year_duration_in_years * 24 * 60 * 60 * 1000
    solar_cycle_year_duration_in_years_in_microseconds = solar_cycle_year_duration_in_years * 24 * 60 * 60 * 1000 * 1000
    solar_cycle_year_duration_in_years_in_nanoseconds = solar_cycle_year_duration_in_years * 24 * 60 * 60 * 1000 * 1000 * 1000
    solar_cycle_year_duration_in_years_in_picoseconds = solar_cycle_year_duration_in_years * 24 * 60 * 60 * 1000 * 1000 * 1000 * 1000
    solar_cycle_year_duration_in_years_in_femtoseconds = solar_cycle_year_duration_in_years * 24 * 60 * 60 * 1000 * 1000 * 1000 * 1000 * 1000
    solar_cycle_year_duration_in_years_in_attoseconds = solar_cycle_year_duration_in_years * 24 * 60 * 60 * 1000 * 1000 * 1000 * 1000 * 1000 * 1000
    solar_cycle_year_duration_in_years_in_zeptoseconds = solar_cycle_year_duration_in_years * 24 * 60 * 60 * 1000 * 1000 * 1000 * 1000 * 1000 * 1000 * 1000
    solar_cycle_year_duration_in_years_in_yoctoseconds = solar_cycle_year_duration_in_years * 24 * 60 * 60 * 1000 * 1000 * 1000 * 1000 * 1000 * 1000 * 1000 * 1000
    solar_cycle_year_duration_in_years_in_seconds_fraction = solar_cycle_year_duration_in_years * 365.25 * 24 * 60 * 60
    solar_