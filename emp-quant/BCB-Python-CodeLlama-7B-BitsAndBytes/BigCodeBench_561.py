
import pytz
from dateutil import parser

def task_func(date_str, from_tz, to_tz):
    # Parse the input date string
    dt = parser.parse(date_str)

    # Convert the datetime to the specified timezone
    dt_tz = dt.astimezone(pytz.timezone(to_tz))

    # Format the converted datetime as a string
    dt_str = dt_tz.strftime("%Y-%m-%d %H:%M:%S")

    return dt_str