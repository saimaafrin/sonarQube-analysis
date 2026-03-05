
from random import choice
import pytz
from dateutil.parser import parse
# Constants
TIMEZONES = ['America/New_Your', 'Europe/London', 'Asia/Shanghai', 'Asia/Tokyo', 'Australia/Sydney']
def task_func(date_str, from_tz):
    # Parse the input datetime string
    datetime_obj = parse(date_str)
    # Get a random timezone from the list of timezones
    to_tz = choice(TIMEZONES)
    # Convert the datetime object to the new timezone
    converted_datetime = datetime_obj.astimezone(pytz.timezone(to_tz))
    # Return a tuple of the converted datetime and the randomly chosen timezone
    return (converted_datetime, to_tz)