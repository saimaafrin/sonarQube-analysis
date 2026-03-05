from random import choice
import pytz
from dateutil.parser import parse
TIMEZONES = ['America/New_York', 'Europe/London', 'Asia/Shanghai', 'Asia/Tokyo', 'Australia/Sydney']
def task_func(date_str, from_tz):
    # Parse the input date string to a datetime object in the specified timezone
    from_tz_obj = pytz.timezone(from_tz)
    dt = from_tz_obj.localize(parse(date_str))
    
    # Randomly choose a target timezone
    to_tz = choice(TIMEZONES)
    to_tz_obj = pytz.timezone(to_tz)
    
    # Convert the datetime object to the target timezone
    dt_converted = dt.astimezone(to_tz_obj)
    
    # Format the converted datetime object as a string
    converted_date_str = dt_converted.strftime('%Y-%m-%d %H:%M:%S %Z%z')
    
    # Return the converted datetime string and the target timezone
    return (converted_date_str, to_tz)