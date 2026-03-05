
from datetime import datetime, timedelta
import pytz
import calendar

def task_func(days_in_past=7):
    if days_in_past < 0:
        raise ValueError("days_in_past must be a non-negative integer")
    
    # Get the current UTC time
    utc_now = datetime.now(pytz.utc)
    
    # Calculate the date 'days_in_past' days ago
    target_date = utc_now - timedelta(days=days_in_past)
    
    # Get the weekday name
    weekday_name = calendar.day_name[target_date.weekday()]
    
    return weekday_name