import pandas as pd
from datetime import datetime
import holidays
def task_func(start_date=datetime(2023, 1, 1), end_date=datetime(2023, 12, 31), country='US'):
    # Validate input types and order
    if not isinstance(start_date, datetime) or not isinstance(end_date, datetime):
        raise ValueError("start_date and end_date must be datetime objects")
    if start_date > end_date:
        raise ValueError("start_date must be before end_date")

    # Create a list of public holidays for the specified country
    country_holidays = holidays.CountryHoliday(country)

    # Generate a date range and filter out weekends and public holidays
    date_range = pd.date_range(start=start_date, end=end_date)
    business_days = [date for date in date_range if date.weekday() < 5 and date not in country_holidays]

    return business_days