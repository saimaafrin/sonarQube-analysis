import pandas as pd
from datetime import datetime
import holidays
def task_func(start_date=datetime(2023, 1, 1), end_date=datetime(2023, 12, 31), country='US'):
    """
    Create a list of business days between two dates, excluding weekends and specified country's public holidays.
    """
    if not isinstance(start_date, datetime):
        raise ValueError("start_date must be a datetime object")
    if not isinstance(end_date, datetime):
        raise ValueError("end_date must be a datetime object")
    if start_date > end_date:
        raise ValueError("start_date must be before end_date")

    # Fetch public holidays for the specified country
    holidays_df = holidays.fetch_holidays(country)

    # Create a list of business days between start_date and end_date
    business_days = []
    for date in pd.date_range(start_date, end_date):
        if date.weekday() not in [5, 6] and date not in holidays_df:
            business_days.append(date)

    return business_days
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)
country = 'US'