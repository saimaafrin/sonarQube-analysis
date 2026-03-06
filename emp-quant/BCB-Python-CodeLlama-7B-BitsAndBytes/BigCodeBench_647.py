
import pytz
from dateutil.parser import parse

def task_func(date_str, from_tz, to_tz):
    # Parse the date string into a datetime object
    dt = parse(date_str)

    # Convert the datetime object from the source time zone to the destination time zone
    dt_to_tz = dt.astimezone(pytz.timezone(to_tz))

    # Calculate the time difference in seconds between the two time zones
    diff = dt_to_tz - dt

    # Return the time difference in seconds
    return diff.total_seconds()