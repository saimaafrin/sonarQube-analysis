import pandas as pd
from datetime import datetime
import holidays
def task_func(start_date=datetime(2023, 1, 1), end_date=datetime(2023, 12, 31), country='US'):
    # Validate input types and order
    if not isinstance(start_date, datetime) or not isinstance(end_date, datetime):
        raise ValueError("start_date and end_date must be datetime objects")
    if start_date > end_date:
        raise ValueError("start_date must be before end_date")

    # Create a list of business days
    country_holidays = holidays.CountryHoliday(country)
    business_days = pd.date_range(start=start_date, end=end_date, freq='B')
    business_days = business_days[~business_days.isin(country_holidays)]

    return business_days.tolist()