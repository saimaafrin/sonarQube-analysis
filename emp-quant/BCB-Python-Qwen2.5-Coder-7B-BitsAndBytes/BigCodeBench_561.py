
import pytz
from dateutil import parser

def task_func(date_str, from_tz, to_tz):
    # Parse the input date string into a datetime object
    dt = parser.parse(date_str)
    
    # Create timezone objects for the source and target timezones
    from_timezone = pytz.timezone(from_tz)
    to_timezone = pytz.timezone(to_tz)
    
    # Localize the datetime object to the source timezone
    dt = from_timezone.localize(dt)
    
    # Convert the datetime object to the target timezone
    dt_converted = dt.astimezone(to_timezone)
    
    # Format the converted datetime object as a string in "yyyy-mm-dd hh:mm:ss" format
    result = dt_converted.strftime("%Y-%m-%d %H:%M:%S")
    
    return result