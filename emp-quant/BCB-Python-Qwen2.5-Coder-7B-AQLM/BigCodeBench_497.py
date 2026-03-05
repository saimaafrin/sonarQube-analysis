
from datetime import datetime, timedelta
import pytz
import calendar

def task_func(days_in_past=7):
    if days_in_past < 0:
        raise ValueError("days_in_past must be a non-negative integer")
    
    # Get the current UTC time
    utc_now = datetime.now(pytz.utc)
    
    # Calculate the target date 'days_in_past' days ago
    target_date = utc_now - timedelta(days=days_in_past)
    
    # Get the weekday of the target date
    weekday_number = target_date.weekday()
    weekday_name = calendar.day_name[weekday_number]
    
    return weekday_name