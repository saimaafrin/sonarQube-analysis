
import pytz
import numpy as np
from dateutil.parser import parse
import math
MOON_PHASES_YEARS = np.array([1987, 1994, 2001, 2008, 2015, 2022])
def task_func(date_str, from_tz, to_tz):
    date = parse(date_str)
    date_utc = date.astimezone(pytz.utc)
    year = date_utc.year
    month = date_utc.month
    day = date_utc.day
    hour = date_utc.hour
    minute = date_utc.minute
    second = date_utc.second
    phase_index = np.where(MOON_PHASES_YEARS == year)[0][0]
    phase_offset = (month - 1) * 30 + (day - 1) * 2 + (hour - 1) * 24 + (minute - 1) * 60 + (second - 1) * 60
    phase_offset = phase_offset % 28 * 28
    phase = phase_offset / 28
    return phase