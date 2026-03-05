
import pytz
from dateutil.parser import parse

def task_func(date_str, from_tz, to_tz):
    # Parse the date string into a datetime object
    dt = parse(date_str)
    
    # Set the time zones
    from_tz = pytz.timezone(from_tz)
    to_tz = pytz.timezone(to_tz)
    
    # Localize the datetime object to the source time zone
    dt = from_tz.localize(dt)
    
    # Convert the datetime object to the destination time zone
    dt_to_tz = dt.astimezone(to_tz)
    
    # Get the current time in the destination time zone
    now_to_tz = to_tz.localize(dt_to_tz.now())
    
    # Calculate the time difference in seconds
    time_difference = (now_to_tz - dt_to_tz).total_seconds()
    
    return int(time_difference)