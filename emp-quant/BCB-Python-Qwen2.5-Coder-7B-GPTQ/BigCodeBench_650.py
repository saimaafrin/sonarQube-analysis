from datetime import datetime
import pytz
from dateutil.parser import parse
def task_func(date_str, tz_str):
    # Parse the input date string into a datetime object
    dt = parse(date_str)
    
    # Create a timezone object from the provided timezone string
    tz = pytz.timezone(tz_str)
    
    # Localize the datetime object to the specified timezone
    dt = dt.replace(tzinfo=pytz.utc).astimezone(tz)
    
    # Calculate the next New Year's Day in the specified timezone
    next_new_year = dt.replace(year=dt.year + 1, month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
    if dt > next_new_year:
        next_new_year += timedelta(days=365)  # If today is already past New Year, add one year
    
    # Calculate the time difference in seconds until the next New Year
    time_until_new_year = (next_new_year - dt).total_seconds()
    
    return int(time_until_new_year)