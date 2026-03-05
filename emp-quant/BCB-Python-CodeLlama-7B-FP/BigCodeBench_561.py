import pytz
from dateutil import parser
def task_func(date_str, from_tz, to_tz):
    """
    Converts a date time from one timezone to another.
    """
    # Parse the input date string into a datetime object
    dt = parser.parse(date_str)

    # Convert the datetime object to the specified timezone
    dt_converted = dt.astimezone(pytz.timezone(to_tz))

    # Format the converted datetime object into a string
    dt_str = dt_converted.strftime("%Y-%m-%d %H:%M:%S")

    return dt_str