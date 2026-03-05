import pytz
from dateutil import parser
def task_func(date_str, from_tz, to_tz):
    """
    Converts a date time from one timezone to another.
    """
    # Parse the date string into a datetime object
    date_obj = parser.parse(date_str)

    # Convert the datetime object to the specified timezone
    converted_date = date_obj.astimezone(pytz.timezone(to_tz))

    # Format the converted datetime object into a string
    converted_date_str = converted_date.strftime("%Y-%m-%d %H:%M:%S")

    return converted_date_str