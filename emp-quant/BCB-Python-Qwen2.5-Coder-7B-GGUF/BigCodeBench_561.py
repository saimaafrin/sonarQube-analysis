
import pytz
from dateutil import parser

def task_func(date_str, from_tz, to_tz):
    # Parse the input date string into a datetime object
    dt = parser.parse(date_str)
    
    # Set the timezone of the datetime object
    from_tz_obj = pytz.timezone(from_tz)
    dt = from_tz_obj.localize(dt)
    
    # Convert the datetime object to the target timezone
    to_tz_obj = pytz.timezone(to_tz)
    dt = dt.astimezone(to_tz_obj)
    
    # Format the datetime object to the desired string format
    converted_date_str = dt.strftime("%Y-%m-%d %H:%M:%S")
    
    return converted_date_str