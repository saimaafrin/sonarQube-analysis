
import pandas as pd
from datetime import datetime
import holidays

def task_func(start_date=datetime(2023, 1, 1), end_date=datetime(2023, 12, 31), country='US'):
    # Check if start_date and end_date are valid datetime objects
    if not isinstance(start_date, datetime) or not isinstance(end_date, datetime):
        raise ValueError("start_date and end_date must be datetime objects")
    if start_date > end_date:
        raise ValueError("start_date must be before end_date")

    # Create a list of business days between start_date and end_date
    business_days = []
    for date in pd.date_range(start_date, end_date):
        if date.weekday() not in (5, 6) and date not in holidays.holidays(country=country):
            business_days.append(date)

    return business_days