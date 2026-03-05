import pytz
import numpy as np
from dateutil.parser import parse
import math
def task_func(date_str, from_tz, to_tz):
    # Parse the input date string to a datetime object
    date_obj = parse(date_str)
    
    # Convert the datetime object from the source timezone to the target timezone
    from_tz = pytz.timezone(from_tz)
    to_tz = pytz.timezone(to_tz)
    date_obj = date_obj.replace(tzinfo=from_tz)
    date_obj = date_obj.astimezone(to_tz)
    
    # Calculate the Julian day number for the given date
    year = date_obj.year
    month = date_obj.month
    day = date_obj.day
    hour = date_obj.hour
    minute = date_obj.minute
    second = date_obj.second
    
    a = (14 - month) // 12
    y = year + 4800 - a
    m = month + 12*a - 3
    
    jd = day + ((153*m + 2) // 5) + 365*y + (y // 4) - (y // 100) + (y // 400) - 32045
    jd += (hour - 12) / 24 + minute / 1440 + second / 86400
    
    # Calculate the moon phase using the Julian day number
    T = (jd - 2451550.1) / 29.53058867
    moon_phase = (T - math.floor(T)) % 1
    
    return moon_phase