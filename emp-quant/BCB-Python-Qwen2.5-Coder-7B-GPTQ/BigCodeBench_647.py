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
    current_time = pytz.timezone(to_tz).localize(dt_to_tz.replace(hour=0, minute=0, second=0, microsecond=0))
    
    # Calculate the time difference in seconds
    time_difference = (dt_to_tz - current_time).total_seconds()
    
    return int(time_difference)