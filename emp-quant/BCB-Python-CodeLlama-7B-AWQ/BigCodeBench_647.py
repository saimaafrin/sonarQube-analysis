import pytz
from dateutil.parser import parse
def task_func(date_str, from_tz, to_tz):
    """
    Convert a date string from one time zone to another and return the time difference in seconds to the current time in the destination time zone.
    """
    # Parse the date string into a datetime object
    date = parse(date_str)

    # Convert the datetime object to the destination time zone
    dest_time = date.astimezone(pytz.timezone(to_tz))

    # Get the current time in the destination time zone
    now = pytz.timezone(to_tz).localize(pytz.utc.localize(datetime.utcnow()))

    # Calculate the time difference in seconds
    diff = (dest_time - now).total_seconds()

    return diff