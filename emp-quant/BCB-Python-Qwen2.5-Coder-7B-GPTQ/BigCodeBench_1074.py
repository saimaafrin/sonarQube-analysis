import pytz
from dateutil.parser import parse
TIME_FORMAT = "%d/%m/%y %H:%M:%S.%f"
def task_func(time_string, from_tz, to_tz):
    # Parse the input time string into a datetime object
    dt = parse(time_string)
    
    # Set the timezone for the input datetime object
    dt = dt.replace(tzinfo=pytz.timezone(from_tz))
    
    # Convert the datetime object to the target timezone
    dt = dt.astimezone(pytz.timezone(to_tz))
    
    # Format the datetime object as a string in the required format
    return dt.strftime(TIME_FORMAT)