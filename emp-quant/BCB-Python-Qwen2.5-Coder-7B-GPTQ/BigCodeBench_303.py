import pytz
import numpy as np
from dateutil.parser import parse
import math
def task_func(date_str, from_tz, to_tz):
    # Parse the input date string to a datetime object
    date = parse(date_str)
    
    # Convert the datetime object from the from_tz timezone to the to_tz timezone
    to_tz = pytz.timezone(to_tz)
    date = date.replace(tzinfo=pytz.timezone(from_tz)).astimezone(to_tz)
    
    # Calculate the number of days since the reference year 1987
    days_since_1987 = (date - parse('1987-01-01')).days
    
    # Calculate the moon phase using the number of days since 1987
    moon_phase = (days_since_1987 / 29.53) % 1
    
    return moon_phase