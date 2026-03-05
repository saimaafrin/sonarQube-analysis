import pytz
from dateutil import parser
def task_func(date_str, from_tz, to_tz):
    # Parse the input date string into a datetime object
    dt = parser.parse(date_str)
    
    # Create timezone objects for the source and target timezones
    from_tz = pytz.timezone(from_tz)
    to_tz = pytz.timezone(to_tz)
    
    # Localize the datetime object to the source timezone
    dt = from_tz.localize(dt)
    
    # Convert the datetime object to the target timezone
    dt = dt.astimezone(to_tz)
    
    # Format the datetime object as a string in the desired format
    return dt.strftime("%Y-%m-%d %H:%M:%S")