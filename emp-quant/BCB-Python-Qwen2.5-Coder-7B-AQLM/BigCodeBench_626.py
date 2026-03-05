
from random import choice
import pytz
from dateutil.parser import parse

# Constants
TIMEZONES = ['America/New_York', 'Europe/London', 'Asia/Shanghai', 'Asia/Tokyo', 'Australia/Sydney']

def task_func(date_str, from_tz):
    # Parse the input date string into a datetime object in the specified timezone
    from_tz_obj = pytz.timezone(from_tz)
    dt = from_tz_obj.localize(parse(date_str))
    
    # Choose a random timezone from the list
    to_tz = choice(TIMEZONES)
    to_tz_obj = pytz.timezone(to_tz)
    
    # Convert the datetime object to the randomly chosen timezone
    dt_converted = dt.astimezone(to_tz_obj)
    
    # Return the converted datetime string and the randomly chosen timezone
    return (dt_converted.strftime('%Y-%m-%d %H:%M:%S %Z%z'), to_tz)