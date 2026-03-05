
import pytz
from dateutil import parser

def convert_datetime(date_str, from_tz, to_tz):
    """
    Converts a date time from one timezone to another.

    Args:
        date_str (str): The date time string in "yyyy-mm-dd hh:mm:ss" format.
        from_tz (str): The timezone to convert from.
        to_tz (str): The timezone to convert to.

    Returns:
        str: The converted datetime string in "yyyy-mm-dd hh:mm:ss" format.
    """
    # Parse the date time string
    dt = parser.parse(date_str)

    # Convert the datetime to the specified timezone
    dt_tz = pytz.timezone(from_tz)
    dt_tz = dt_tz.localize(dt)
    dt_tz = dt_tz.astimezone(pytz.timezone(to_tz))

    # Format the converted datetime
    return dt_tz.strftime("%Y-%m-%d %H:%M:%S")