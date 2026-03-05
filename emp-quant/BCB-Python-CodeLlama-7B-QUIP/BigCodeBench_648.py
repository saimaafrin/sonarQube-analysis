
from dateutil.parser import parse
from datetime import timedelta

def get_next_business_day(date_str):
    date = parse(date_str)
    if date.weekday() in (5, 6):
        date += timedelta(days=1)
    return date

date = get_next_business_day("2023-02-27")
print(date)