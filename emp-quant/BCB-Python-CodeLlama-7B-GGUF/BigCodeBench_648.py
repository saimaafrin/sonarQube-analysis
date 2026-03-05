
from dateutil.parser import parse
from datetime import timedelta

def get_next_business_day(date_str):
    date = parse(date_str)
    while date.weekday() not in range(5):  # Monday-Friday
        date += timedelta(days=1)
    return date