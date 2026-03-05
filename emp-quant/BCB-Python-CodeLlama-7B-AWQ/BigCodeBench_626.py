from random import choice
import pytz
from dateutil.parser import parse
TIMEZONES = ['America/New_York', 'Europe/London', 'Asia/Shanghai', 'Asia/Tokyo', 'Australia/Sydney']
def task_func(date_str, from_tz):
    """
    Converts a datetime string from a given timezone to a datetime string in a randomly chosen timezone.
    """
    # Parse the input date string
    date = parse(date_str)

    # Convert the input date to the specified timezone
    date = date.astimezone(pytz.timezone(from_tz))

    # Choose a random timezone from the list of available timezones
    to_tz = choice(TIMEZONES)

    # Convert the date to the chosen timezone
    date = date.astimezone(pytz.timezone(to_tz))

    # Return a tuple containing the converted datetime string and the randomly chosen timezone
    return (date.strftime("%Y-%m-%d %H:%M:%S"), to_tz)