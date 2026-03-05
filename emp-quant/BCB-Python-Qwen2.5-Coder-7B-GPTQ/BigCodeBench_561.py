import pytz
from dateutil import parser
def task_func(date_str, from_tz, to_tz):
    # Parse the input date string into a datetime object
    dt = parser.parse(date_str)
    
    # Set the timezone of the datetime object
    dt = dt.replace(tzinfo=pytz.timezone(from_tz))
    
    # Convert the datetime object to the target timezone
    dt_converted = dt.astimezone(pytz.timezone(to_tz))
    
    # Format the converted datetime object as a string in "yyyy-mm-dd hh:mm:ss" format
    return dt_converted.strftime("%Y-%m-%d %H:%M:%S")