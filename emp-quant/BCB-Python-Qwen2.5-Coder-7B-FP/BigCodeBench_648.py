from dateutil.parser import parse
from datetime import timedelta
def task_func(date_str):
    # Parse the input date string into a datetime object
    date_obj = parse(date_str)
    
    # Loop until we find a weekday (Monday to Friday)
    while date_obj.weekday() >= 5:  # 5 and 6 represent Saturday and Sunday respectively
        date_obj += timedelta(days=1)  # Increment the date by one day
    
    return date_obj