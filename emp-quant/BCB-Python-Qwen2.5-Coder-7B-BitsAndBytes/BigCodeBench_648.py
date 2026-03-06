
from dateutil.parser import parse
from datetime import timedelta

def task_func(date_str):
    # Parse the input date string into a datetime object
    current_date = parse(date_str)
    
    # Define the days of the week as integers (0=Monday, 6=Sunday)
    weekdays = [1, 2, 3, 4, 5]  # Monday to Friday
    
    # Loop until we find the next business day
    while current_date.weekday() not in weekdays:
        current_date += timedelta(days=1)
    
    return current_date