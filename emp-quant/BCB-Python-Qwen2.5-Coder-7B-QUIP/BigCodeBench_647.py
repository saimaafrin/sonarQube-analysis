
import pytz
from dateutil.parser import parse

def task_func(date_str, from_tz, to_tz):
    # Parse the date string into a datetime object in the from_tz
    dt = parse(date_str)
    from_tz = pytz.timezone(from_tz)
    dt = from_tz.localize(dt, is_dst=None)
    
    # Convert the datetime object to the to_tz
    to_tz = pytz.timezone(to_tz)
    dt_to_tz = dt.astimezone(to_tz)
    
    # Get the current time in the to_tz
    current_time_to_tz = datetime.datetime.now(pytz.timezone(to_tz))
    
    # Calculate the time difference in seconds
    time_difference = (dt_to_tz - current_time_to_tz).total_seconds()
    
    return int(time_difference)