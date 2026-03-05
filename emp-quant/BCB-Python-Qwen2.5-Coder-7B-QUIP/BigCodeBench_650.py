
from datetime import datetime
import pytz
from dateutil.parser import parse

def task_func(date_str, tz_str):
    # Parse the input date string into a datetime object
    current_date = parse(date_str)
    
    # Set the target timezone
    target_tz = pytz.timezone(tz_str)
    
    # Convert the current date to the target timezone
    current_date = current_tz.localize(current_date)
    
    # Calculate the next New Year's Day in the target timezone
    next_new_year = current_date.replace(year=current_date.year + 1, month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
    
    # If the current date is already in the next year, calculate for the next year
    if current_date >= next_new_year:
        next_new_year = next_new_year.replace(year=next_new_year.year + 1)
    
    # Calculate the time difference in seconds until the next New Year
    time_until_new_year = (next_new_year - current_date).total_seconds()
    
    return int(time_until_new_year)