
import pandas as pd
from datetime import datetime
import holidays

def task_func(start_date=datetime(2023, 1, 1), end_date=datetime(2023, 12, 31), country='US'):
    # Validate the input dates
    if not isinstance(start_date, datetime):
        raise ValueError("start_date must be a datetime object")
    if not isinstance(end_date, datetime):
        raise ValueError("end_date must be a datetime object")
    if start_date > end_date:
        raise ValueError("start_date must be before end_date")

    # Create a date range
    date_range = pd.date_range(start=start_date, end=end_date)

    # Get the country's public holidays
    country_holidays = holidays.CountryHolidays(country=country)

    # Filter out the weekends and public holidays
    business_days = [date for date in date_range if date.dayofweek < 5 and date not in country_holidays]

    return business_days