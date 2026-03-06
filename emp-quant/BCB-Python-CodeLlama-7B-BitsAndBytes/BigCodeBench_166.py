
import pandas as pd
from datetime import datetime
import holidays

def task_func(start_date=datetime(2023, 1, 1), end_date=datetime(2023, 12, 31), country='US'):
    if not isinstance(start_date, datetime):
        raise ValueError("Start date must be a datetime object")
    if not isinstance(end_date, datetime):
        raise ValueError("End date must be a datetime object")
    if start_date > end_date:
        raise ValueError("Start date must be before end date")

    # Create a list of business days between start_date and end_date
    business_days = []
    for date in pd.date_range(start_date, end_date):
        if date.weekday() < 5 and not holidays.is_holiday(date, country):
            business_days.append(date)

    return business_days