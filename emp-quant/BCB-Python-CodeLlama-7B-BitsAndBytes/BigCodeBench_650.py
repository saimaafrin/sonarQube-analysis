
from datetime import datetime
import pytz
from dateutil.parser import parse

def task_func(date_str, tz_str):
    # Parse the date string and timezone string
    date = parse(date_str)
    tz = pytz.timezone(tz_str)

    # Convert the date to the specified timezone
    date_tz = date.astimezone(tz)

    # Get the start of the year in the specified timezone
    start_of_year = datetime(date_tz.year, 1, 1, 0, 0, 0, tzinfo=tz)

    # Calculate the time until the next year in seconds
    time_until_next_year = (start_of_year - date_tz).total_seconds()

    return int(time_until_next_year)