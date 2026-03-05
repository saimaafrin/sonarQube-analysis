import pytz
from dateutil.parser import parse
def task_func(date_str, from_tz, to_tz):
    # Parse the date string into a datetime object
    dt = parse(date_str)
    
    # Set the timezones
    from_tz = pytz.timezone(from_tz)
    to_tz = pytz.timezone(to_tz)
    
    # Localize the datetime object to the from_tz timezone
    dt = from_tz.localize(dt)
    
    # Convert the datetime object to the to_tz timezone
    dt_to_tz = dt.astimezone(to_tz)
    
    # Get the current time in the to_tz timezone
    now_to_tz = to_tz.localize(dt_to_tz.now())
    
    # Calculate the time difference in seconds
    time_difference = (now_to_tz - dt_to_tz).total_seconds()
    
    return int(time_difference)