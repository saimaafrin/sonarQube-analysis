
from dateutil.parser import parse
from datetime import timedelta

def task_func(date_str):
    # Parse the input date string into a datetime object
    current_date = parse(date_str)
    
    # Define the number of days to add to get to the next business day
    days_to_add = 0
    
    # Check if the current date is a weekend (Saturday or Sunday)
    while current_date.weekday() >= 5:  # 5 corresponds to Saturday, 6 to Sunday
        current_date += timedelta(days=1)
    
    # Return the next business day as a datetime object
    return current_date