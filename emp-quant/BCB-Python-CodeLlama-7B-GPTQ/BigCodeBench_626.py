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

    # Get a random timezone from the list of timezones
    to_tz = choice(TIMEZONES)

    # Convert the date to the random timezone
    converted_date = date.astimezone(pytz.timezone(to_tz))

    # Return a tuple containing the converted date and the random timezone
    return (converted_date, to_tz)