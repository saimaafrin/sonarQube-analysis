
import pytz
from dateutil.parser import parse

def task_func(date_str, from_tz, to_tz):
    # Parse the date string into a datetime object
    dt = parse(date_str)
    
    # Set the source timezone
    source_tz = pytz.timezone(from_tz)
    dt = source_tz.localize(dt)
    
    # Convert the datetime to the target timezone
    target_tz = pytz.timezone(to_tz)
    dt_target = dt.astimezone(target_tz)
    
    # Get the current time in the target timezone
    now_target = target_tz.localize(datetime.now())
    
    # Calculate the time difference in seconds
    time_difference = (now_target - dt_target).total_seconds()
    
    return int(time_difference)