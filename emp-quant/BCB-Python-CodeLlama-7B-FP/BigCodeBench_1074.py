import pytz
from dateutil.parser import parse
TIME_FORMAT = "%d/%m/%y %H:%M:%S.%f"
def task_func(time_string, from_tz, to_tz):
    """
    Converts a time string from one timezone to another, considering various cases such as daylight saving time.
    """
    # Parse the time string into a datetime object
    dt = parse(time_string, TIME_FORMAT)
    # Convert the datetime object to the source timezone
    dt_src = dt.astimezone(pytz.timezone(from_tz))
    # Convert the datetime object to the target timezone
    dt_dst = dt_src.astimezone(pytz.timezone(to_tz))
    # Format the converted datetime object into the desired format
    return dt_dst.strftime(TIME_FORMAT)