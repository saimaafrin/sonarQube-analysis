
from random import choice
import pytz
from dateutil.parser import parse

# Constants
TIMEZONES = ['America/New_York', 'Europe/London', 'Asia/Shanghai', 'Asia/Tokyo', 'Australia/Sydney']

def task_func(date_str, from_tz):
    # Parse the input date string and convert it to a datetime object
    dt = parse(date_str)

    # Convert the datetime object to the desired timezone
    to_tz = choice(TIMEZONES)
    dt_in_to_tz = dt.astimezone(pytz.timezone(to_tz))

    # Return a tuple containing the converted datetime string and the randomly chosen timezone
    return (dt_in_to_tz.strftime('%Y-%m-%d %H:%M:%S'), to_tz)