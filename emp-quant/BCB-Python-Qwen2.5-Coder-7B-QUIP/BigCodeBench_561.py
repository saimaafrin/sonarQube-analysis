
import pytz
from dateutil import parser

def task_func(date_str, from_tz, to_tz):
    # Parse the input date string into a datetime object
    date_obj = parser.parse(date_str)
    
    # Create timezone objects for the from and to timezones
    from_tz = pytz.timezone(from_tz)
    to_tz = pytz.timezone(to_tz)
    
    # Localize the datetime object to the from timezone
    localized_date = from_tz.localize(date_obj, is_dst=None)
    
    # Convert the localized datetime to the to timezone
    converted_date = localized_date.astimezone(to_tz)
    
    # Format the converted datetime as a string in the desired format
    formatted_date = converted_date.strftime("%Y-%m-%d %H:%M:%S")
    
    return formatted_date