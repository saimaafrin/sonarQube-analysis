
from datetime import datetime
import pytz
from dateutil.parser import parse

def task_func(date_str, tz_str):
    # Parse the input date string into a datetime object
    date = parse(date_str)
    
    # Create a timezone object from the input timezone string
    timezone = pytz.timezone(tz_str)
    
    # Localize the datetime object to the specified timezone
    localized_date = timezone.localize(date)
    
    # Calculate the next New Year's Day in the specified timezone
    next_new_year = localized_date.replace(year=localized_date.year + 1, month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
    
    # If the current date is already past New Year's Day, move to the next year
    if localized_date > next_new_year:
        next_new_year = next_new_year.replace(year=next_new_year.year + 1)
    
    # Calculate the time difference in seconds until the next New Year
    time_until_new_year = (next_new_year - localized_date).total_seconds()
    
    return int(time_until_new_year)