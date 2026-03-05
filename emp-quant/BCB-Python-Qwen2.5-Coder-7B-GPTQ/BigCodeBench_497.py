from datetime import datetime, timedelta
import pytz
import calendar
def task_func(days_in_past=7):
    if days_in_past < 0:
        raise ValueError("days_in_past must be a non-negative integer")
    
    # Get the current UTC time
    now_utc = datetime.now(pytz.utc)
    
    # Calculate the date 'days_in_past' days ago
    target_date_utc = now_utc - timedelta(days=days_in_past)
    
    # Get the weekday as an integer (0=Monday, 6=Sunday)
    weekday_int = target_date_utc.weekday()
    
    # Map the integer to the corresponding weekday name
    weekday_name = calendar.day_name[weekday_int]
    
    return weekday_name