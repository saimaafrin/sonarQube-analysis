
from datetime import datetime, timedelta
import pytz
import calendar

def task_func(days_in_past=7):
    if days_in_past < 0:
        raise ValueError("'days_in_past' must be positive")
    utc_now = datetime.utcnow().replace(tzinfo=pytz.utc)
    target_date = utc_now - timedelta(days=days_in_past)
    target_weekday = calendar.weekday(target_date)
    return calendar.weekday_name[target_weekday]