
from datetime import datetime, timedelta
import pytz
import calendar

def get_weekday(days_in_past=7):
    if days_in_past < 0:
        raise ValueError("'days_in_past' must be non-negative")
    utc_now = datetime.now(pytz.utc)
    target_date = utc_now - timedelta(days=days_in_past)
    weekday = calendar.day_name[target_date.weekday()]
    return weekday