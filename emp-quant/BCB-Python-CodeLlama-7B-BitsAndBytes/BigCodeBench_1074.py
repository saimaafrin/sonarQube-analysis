
import pytz
from dateutil.parser import parse

# Constants
TIME_FORMAT = "%d/%m/%y %H:%M:%S.%f"

def task_func(time_string, from_tz, to_tz):
    # Parse the time string into a datetime object
    dt = parse(time_string, TIME_FORMAT)

    # Convert the datetime object to the source timezone
    src_tz = pytz.timezone(from_tz)
    dt_src = src_tz.localize(dt)

    # Convert the datetime object to the target timezone
    dst_tz = pytz.timezone(to_tz)
    dt_dst = dst_tz.normalize(dt_src.astimezone(dst_tz))

    # Format the converted datetime object into a string
    converted_time = dt_dst.strftime(TIME_FORMAT)

    return converted_time

print(task_func(time_string, from_tz, to_tz))