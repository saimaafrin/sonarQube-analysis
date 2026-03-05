
from dateutil.parser import parse
from datetime import timedelta

def task_func(date_str):
    # Parse the input date string into a datetime object
    date_obj = parse(date_str)
    
    # Loop until we find the next business day (Monday to Friday)
    while date_obj.weekday() >= 5:  # 5 corresponds to Saturday, 6 to Sunday
        date_obj += timedelta(days=1)
    
    # Return the datetime object of the next business day
    return date_obj