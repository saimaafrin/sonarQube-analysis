import pytz
from dateutil.parser import parse
TIME_FORMAT = "%d/%m/%y %H:%M:%S.%f"
def task_func(time_string, from_tz, to_tz):
    # Parse the input time string into a datetime object
    original_time = parse(time_string, fuzzy=True)
    
    # Set the original timezone
    original_tz = pytz.timezone(from_tz)
    original_time = original_tz.localize(original_time)
    
    # Convert the time to the target timezone
    target_tz = pytz.timezone(to_tz)
    converted_time = original_time.astimezone(target_tz)
    
    # Format the converted time as a string
    formatted_time = converted_time.strftime(TIME_FORMAT)
    
    return formatted_time