
import pytz
from dateutil.parser import parse

def task_func(date_str, from_tz, to_tz):
    # Parse the date string into a datetime object
    dt = parse(date_str)
    
    # Set the time zone for the datetime object
    from_tz_obj = pytz.timezone(from_tz)
    dt = from_tz_obj.localize(dt)
    
    # Convert the datetime object to the destination time zone
    to_tz_obj = pytz.timezone(to_tz)
    dt_to_tz = dt.astimezone(to_tz_obj)
    
    # Get the current time in the destination time zone
    current_time_to_tz = to_tz_obj.localize(dt_to_tz.now())
    
    # Calculate the time difference in seconds
    time_difference = (current_time_to_tz - dt_to_tz).total_seconds()
    
    return int(time_difference)