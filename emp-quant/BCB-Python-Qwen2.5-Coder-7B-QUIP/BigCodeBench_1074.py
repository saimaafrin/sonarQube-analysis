
import pytz
from dateutil.parser import parse
from datetime import datetime

# Constants
TIME_FORMAT = "%d/%m/%y %H:%M:%S.%f"

def task_func(time_string, from_tz, to_tz):
    # Parse the input time string into a datetime object
    dt = parse(time_string, fuzzy=True)
    
    # Create timezone objects for the from and to timezones
    from_tz = pytz.timezone(from_tz)
    to_tz = pytz.timezone(to_tz)
    
    # Localize the datetime object to the from timezone
    dt = from_tz.localize(dt, is_dst=None)
    
    # Convert the localized datetime object to the to timezone
    dt = dt.astimezone(to_tz)
    
    # Format the converted datetime object to the desired output format
    converted_time_string = dt.strftime(TIME_FORMAT)
    
    return converted_time_string