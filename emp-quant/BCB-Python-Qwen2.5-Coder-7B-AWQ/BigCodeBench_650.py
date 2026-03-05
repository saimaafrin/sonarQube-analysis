from datetime import datetime
import pytz
from dateutil.parser import parse
def task_func(date_str, tz_str):
    # Parse the input date string into a datetime object
    given_date = parse(date_str)
    
    # Create a timezone object using the provided timezone string
    timezone = pytz.timezone(tz_str)
    
    # Localize the given date to the specified timezone
    localized_date = timezone.localize(given_date)
    
    # Calculate the next New Year's date in the specified timezone
    next_new_year = datetime(localized_date.year + 1, 1, 1, tzinfo=timezone)
    
    # If the given date is already past New Year's, set next New Year's to the following year
    if localized_date > next_new_year:
        next_new_year = datetime(localized_date.year + 2, 1, 1, tzinfo=timezone)
    
    # Calculate the time difference in seconds until the next New Year
    time_until_new_year = (next_new_year - localized_date).total_seconds()
    
    # Return the time difference in seconds
    return int(time_until_new_year)