
from datetime import datetime
import pytz
from dateutil.parser import parse

def task_func(date_str, tz_str):
    # Parse the date string and timezone string
    date = parse(date_str)
    tz = pytz.timezone(tz_str)

    # Convert the date to the specified timezone
    tz_date = date.astimezone(tz)

    # Calculate the time until the next New Year in the specified timezone
    next_year = datetime(tz_date.year + 1, 1, 1, 0, 0, 0, tzinfo=tz)
    time_until_next_year = next_year - tz_date

    # Return the time in seconds until the next New Year
    return time_until_next_year.total_seconds()