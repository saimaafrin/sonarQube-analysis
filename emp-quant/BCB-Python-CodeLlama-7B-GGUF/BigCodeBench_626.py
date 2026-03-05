
from random import choice
import pytz
from dateutil.parser import parse
# Constants
TIMEZONES = ['America/New_York', 'Europe/London', 'Asia/Shanghai', 'Asia/Tokyo', 'Australia/Sydney']
def task_func(date_str, from_tz):
    # Parse the input datetime string
    dt = parse(date_str)
    # Convert the datetime to the specified timezone
    dt_in_from_tz = dt.astimezone(pytz.timezone(from_tz))
    # Choose a random timezone from the list of timezones
    to_tz = choice(TIMEZONES)
    # Convert the datetime to the random timezone
    dt_in_to_tz = dt_in_from_tz.astimezone(pytz.timezone(to_tz))
    # Return a tuple containing the converted datetime string and the random timezone
    return (dt_in_to_tz.strftime('%Y-%m-%d %H:%M:%S %Z'), to_tz)