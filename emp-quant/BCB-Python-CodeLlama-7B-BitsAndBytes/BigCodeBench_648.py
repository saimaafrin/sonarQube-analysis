
from dateutil.parser import parse
from datetime import timedelta

def task_func(date_str):
    # Parse the date string using dateutil.parser
    date = parse(date_str)

    # Calculate the number of days until the next business day
    days_to_next_business_day = (date.weekday() + 1) % 5

    # Add the number of days to the current date to get the next business day
    next_business_day = date + timedelta(days_to_next_business_day)

    # Return the datetime object of the next business day
    return next_business_day