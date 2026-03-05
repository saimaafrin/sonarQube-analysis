import pytz
from dateutil.parser import parse
def task_func(date_str, from_tz, to_tz):
    # Parse the date string into a datetime object
    dt = parse(date_str)
    
    # Set the time zone for the datetime object
    dt = dt.replace(tzinfo=pytz.timezone(from_tz))
    
    # Convert the datetime object to the destination time zone
    dt_to_tz = dt.astimezone(pytz.timezone(to_tz))
    
    # Get the current time in the destination time zone
    current_time = pytz.timezone(to_tz).localize(dt_to_tz.now())
    
    # Calculate the time difference in seconds
    time_difference = (current_time - dt_to_tz).total_seconds()
    
    return int(time_difference)