from random import choice
import pytz
from dateutil.parser import parse
TIMEZONES = ['America/New_York', 'Europe/London', 'Asia/Shanghai', 'Asia/Tokyo', 'Australia/Sydney']
def task_func(date_str, from_tz):
    # Parse the input date string to a datetime object in the specified timezone
    dt = parse(date_str).replace(tzinfo=pytz.timezone(from_tz))
    
    # Randomly choose a timezone from the list
    to_tz = choice(TIMEZONES)
    
    # Convert the datetime object to the randomly chosen timezone
    dt_converted = dt.astimezone(pytz.timezone(to_tz))
    
    # Format the converted datetime object as a string
    converted_date_str = dt_converted.strftime('%Y-%m-%d %H:%M:%S %Z%z')
    
    # Return the converted datetime string and the randomly chosen timezone
    return (converted_date_str, to_tz)