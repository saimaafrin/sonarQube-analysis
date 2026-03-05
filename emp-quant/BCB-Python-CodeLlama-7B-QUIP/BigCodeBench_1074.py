
import pytz
from dateutil.parser import parse
# Constants
TIME_FORMAT = "%d/%m/%y %H:%M:%S.%f"
def task_func(time_string, from_tz, to_tz):
    # Parse the time string
    time_obj = parse(time_string, TIME_FORMAT)
    # Convert the time to the target timezone
    time_obj_utc = time_obj.astimezone(pytz.timezone(to_tz))
    # Format the time in the target timezone
    time_str_utc = time_obj_utc.strftime(TIME_FORMAT)
    return time_str_utc