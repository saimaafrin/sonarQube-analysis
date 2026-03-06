
from datetime import datetime, timedelta
import pytz
import calendar

def task_func(days_in_past=7):
    if days_in_past < 0:
        raise ValueError("'days_in_past' must be non-negative")

    # Get the current date in UTC
    now = datetime.now(pytz.utc)

    # Compute the date 'days_in_past' days ago
    target_date = now - timedelta(days=days_in_past)

    # Get the weekday of the target date
    weekday = calendar.day_name[target_date.weekday()]

    return weekday