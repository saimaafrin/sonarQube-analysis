
import pytz
from dateutil.parser import parse

def task_func(date_str, from_tz, to_tz):
    # Parse the date string into a datetime object
    date = parse(date_str)

    # Convert the datetime object to the destination time zone
    dest_time = date.astimezone(pytz.timezone(to_tz))

    # Calculate the time difference in seconds
    diff = dest_time - date

    # Return the time difference in seconds
    return diff.total_seconds()