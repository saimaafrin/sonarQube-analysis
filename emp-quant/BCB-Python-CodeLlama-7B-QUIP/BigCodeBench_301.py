
import pytz
import numpy as np
from dateutil.parser import parse
import math

SOLAR_CYCLE_YEARS = np.array([1986, 1996, 2008, 2019])

def task_func(date_str, from_tz, to_tz):
    date = parse(date_str)
    date_utc = date.astimezone(pytz.utc)
    year = date_utc.year
    solar_cycle_year = np.min(np.abs(SOLAR_CYCLE_YEARS - year))
    solar_cycle_year_start = date_utc.replace(year=solar_cycle_year)
    solar_cycle_year_end = solar_cycle_year_start + np.timedelta(days=365.25)
    solar_cycle_year_start_utc = solar_cycle_year_start.astimezone(pytz.utc)
    solar_cycle_year_end_utc = solar_cycle_year_end.astimezone(pytz.utc)
    solar_cycle_year_start_utc_dt = solar_cycle_year_start_utc.astimezone(from_tz)
    solar_cycle_year_end_utc_dt = solar_cycle_year_end_utc.astimezone(from_tz)
    solar_cycle_year_start_utc_dt_dt = solar_cycle_year_start_utc_dt.astimezone(to_tz)
    solar_cycle_year_end_utc_dt_dt = solar_cycle_year_end_utc_dt.astimezone(to_tz)
    solar_cycle_year_start_utc_dt_dt_dt = solar_cycle_year_start_utc_dt_dt.astimezone(from_tz)
    solar_cycle_year_end_utc_dt_dt = solar_cycle_year_end_utc_dt.astimezone(from_tz)
    solar_cycle_year_start_utc_dt_dt_dt = solar_cycle_year_start_utc_dt_dt.astimezone(to_tz)
    solar_cycle_year_end_utc_dt_dt = solar_cycle_year_end_utc_dt.astimezone(from_tz)
    solar_cycle_year_start_utc_dt_dt_dt = solar_cycle_year_start_utc_dt_dt.astimezone(from_tz)
    solar_cycle_year_end_utc_dt_dt = solar_cycle_year_end_utc_dt.astimezone(from_tz)
    solar_cycle_year_start_utc_dt_dt_dt = solar_cycle_year_start_utc_dt_dt.astimezone(to_tz)
    solar_cycle_year_end_utc_dt_dt = solar_cycle_year_end_utc_dt.astimezone(from_tz)
    solar_cycle_year_start_utc_dt_dt_dt = solar_cycle_year_start_utc_dt_dt.astimezone(from_tz)
    solar_cycle_year_end_utc_dt_dt = solar_cycle_year_end_utc_dt.astimezone(from_tz)
    solar_cycle_year_start_utc_dt_dt_dt = solar_cycle_year_start_utc_dt_dt.astimezone(to_tz)
    solar_cycle_year_end_utc_dt_dt = solar_cycle_year_end_utc_dt.astimezone(from_tz)
    solar_cycle_year_start_utc_dt_dt_dt = solar_cycle_year_start_utc_dt_dt.astimezone(from_tz)
    solar_cycle_year_end_utc_dt_dt = solar_cycle_year_end_utc_dt.astimezone(from_tz)
    solar_cycle_year_start_utc_dt_dt_dt = solar_cycle_year_start_utc_dt_dt.astimezone(to_tz)
    solar_cycle_year_end_utc_dt_dt = solar_cycle_year_end_utc_dt.astimezone(from_tz)
    solar_cycle_year_start_utc_dt_dt_dt = solar_cycle_year_start_utc_dt_dt.astimezone(from_tz)
    solar_cycle_year_end_utc_dt_dt = solar_cycle_year_end_utc_dt.astimezone(from_tz)
    solar_cycle_year_start_utc_dt_dt_dt = solar_cycle_year_start_utc_dt_dt.astimezone(to_tz)
    solar_cycle_year_end_utc_dt_dt = solar_cycle_year_end_utc_dt.astimezone(from_tz)
    solar_cycle_year_start_utc_dt_dt_dt = solar_cycle_year_start_utc_dt_dt.astimezone(from_tz)
    solar_cycle_year_end_utc_dt_dt = solar_