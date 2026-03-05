
import pytz
from dateutil.parser import parse

def task_func(date_str, from_tz, to_tz):
    date_obj = parse(date_str)
    from_tz_obj = pytz.timezone(from_tz)
    to_tz_obj = pytz.timezone(to_tz)
    from_tz_dt = from_tz_obj.localize(date_obj)
    to_tz_dt = to_tz_obj.normalize(from_tz_obj.normalize(date_obj))
    return (to_tz_dt - from_tz_dt).total_seconds()