
from random import choice
import pytz
from dateutil.parser import parse

# Constants
TIMEZONES = ['America/New_York', 'Europe/London', 'Asia/Shanghai', 'Asia/Tokyo', 'Australia/Sydney']

def task_func(date_str, from_tz):
    # Parse the input date string into a datetime object using the provided timezone
    original_dt = parse(date_str)
    original_tz = pytz.timezone(from_tz)
    original_dt = original_tz.localize(original_dt)

    # Choose a random timezone from the list of available timezones
    to_tz = choice(TIMEZONES)
    target_tz = pytz.timezone(to_tz)

    # Convert the datetime object to the new timezone
    converted_dt = original_dt.astimezone(target_tz)

    # Format the converted datetime object as a string
    converted_date_str = converted_dt.strftime('%Y-%m-%d %H:%M:%S %Z%z')

    return (converted_date_str, to_tz)