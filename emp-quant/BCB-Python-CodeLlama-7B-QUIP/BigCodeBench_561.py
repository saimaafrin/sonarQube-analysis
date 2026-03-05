
import pytz
from dateutil import parser

def task_func(date_str, from_tz, to_tz):
    date_obj = parser.parse(date_str)
    from_tz_obj = pytz.timezone(from_tz)
    to_tz_obj = pytz.timezone(to_tz)
    date_obj_converted = from_tz_obj.localize(date_obj).astimezone(to_tz_obj)
    return date_obj_converted.strftime("%Y-%m-%d %H:%M:%S")