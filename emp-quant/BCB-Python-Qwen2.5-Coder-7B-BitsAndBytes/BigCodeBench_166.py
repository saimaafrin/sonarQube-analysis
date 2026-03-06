
import pandas as pd
from datetime import datetime
import holidays

def task_func(start_date=datetime(2023, 1, 1), end_date=datetime(2023, 12, 31), country='US'):
    # Validate input types
    if not isinstance(start_date, datetime) or not isinstance(end_date, datetime):
        raise ValueError("start_date and end_date must be datetime objects.")
    
    # Validate date order
    if start_date > end_date:
        raise ValueError("start_date must be before end_date.")
    
    # Create a date range
    date_range = pd.date_range(start=start_date, end=end_date)
    
    # Get public holidays for the specified country
    country_holidays = holidays.CountryHoliday(country=country)
    
    # Filter out weekends and public holidays
    business_days = [date for date in date_range if date.weekday() < 5 and date not in country_holidays]
    
    return business_days