from random import choice
import pytz
from dateutil.parser import parse
TIMEZONES = ['America/New_York', 'Europe/London', 'Asia/Shanghai', 'Asia/Tokyo', 'Australia/Sydney']
def task_func(date_str, from_tz):
    # Parse the input datetime string into a datetime object in the specified timezone
    dt = parse(date_str)
    from_tz_obj = pytz.timezone(from_tz)
    dt = dt.replace(tzinfo=from_tz_obj)
    
    # Convert the datetime object to a string in the original timezone
    dt_str = dt.strftime('%Y-%m-%d %H:%M:%S %Z%z')
    
    # Randomly choose a different timezone from the list
    to_tz = choice([tz for tz in TIMEZONES if tz != from_tz])
    to_tz_obj = pytz.timezone(to_tz)
    
    # Convert the datetime object to the randomly chosen timezone
    dt_converted = dt.astimezone(to_tz_obj)
    
    # Convert the converted datetime object to a string
    dt_converted_str = dt_converted.strftime('%Y-%m-%d %H:%M:%S %Z%z')
    
    # Return the converted datetime string and the randomly chosen timezone
    return (dt_converted_str, to_tz)