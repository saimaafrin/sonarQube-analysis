
import pytz
from dateutil.parser import parse
# Constants
TIME_FORMAT = "%d/%m/%y %H:%M:%S.%f"

def task_func(time_string, from_tz, to_tz):
    # Parse the input time string into a datetime object
    dt = parse(time_string)
    
    # Set the timezone of the datetime object to the source timezone
    dt = dt.replace(tzinfo=pytz.timezone(from_tz))
    
    # Convert the datetime object to the target timezone
    dt = dt.astimezone(pytz.timezone(to_tz))
    
    # Format the datetime object to the specified format
    converted_time = dt.strftime(TIME_FORMAT)
    
    return converted_time