
from datetime import datetime
import pytz
from dateutil.parser import parse

def task_func(date_str, tz_str):
    date = parse(date_str)
    tz = pytz.timezone(tz_str)
    next_year = datetime(date.year + 1, 1, 1, 0, 0, 0, tz)
    return next_year - date