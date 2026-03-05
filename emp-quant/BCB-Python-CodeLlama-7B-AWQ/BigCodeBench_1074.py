import pytz
from dateutil.parser import parse
TIME_FORMAT = "%d/%m/%y %H:%M:%S.%f"
def task_func(time_string, from_tz, to_tz):
    # Parse the time string
    time = parse(time_string, TIME_FORMAT)
    # Convert the time to the target timezone
    converted_time = time.astimezone(pytz.timezone(to_tz))
    # Format the converted time
    converted_time_string = converted_time.strftime(TIME_FORMAT)
    return converted_time_string