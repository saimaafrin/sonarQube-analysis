
import pytz
import numpy as np
from dateutil.parser import parse
import math

MOON_PHASES_YEARS = np.array([1987, 1994, 2001, 2008, 2015, 2022])

def get_moon_phase(date_str, from_tz, to_tz):
    date = parse(date_str)
    date = date.astimezone(pytz.timezone(from_tz))
    year = date.year
    month = date.month
    day = date.day
    hour = date.hour
    minute = date.minute
    second = date.second
    moon_phase_year = MOON_PHASES_YEARS[np.argmin(np.abs(MOON_PHASES_YEARS - year))]
    moon_phase_month = month - 1
    moon_phase_day = day - 1
    moon_phase_hour = hour
    moon_phase_minute = minute
    moon_phase_second = second
    moon_phase_total_seconds = (moon_phase_year - 1987) * 365.25 * 24 * 60 * 60 + \
                                moon_phase_month * 30.4375 * 24 * 60 * 60 + \
                                moon_phase_day * 24 * 60 * 60 + \
                                moon_phase_hour * 60 * 60 + \
                                moon_phase_minute * 60 + \
                                moon_phase_second
    moon_phase_total_days = moon_phase_total_seconds / (24 * 60 * 60)
    moon_phase = moon_phase_total_days / 29.530588236
    return moon_phase