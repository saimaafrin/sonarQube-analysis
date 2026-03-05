
import pandas as pd
from datetime import datetime
import holidays

def task_func(start_date=datetime(2023, 1, 1), end_date=datetime(2023, 12, 31), country='US'):
    # Validate input dates
    if not isinstance(start_date, datetime) or start_date > end_date:
        raise ValueError("start_date must be a datetime object and must be before end_date")
    if not isinstance(end_date, datetime) or end_date < start_date:
        raise ValueError("end_date must be a datetime object and must be after start_date")
    
    # Create a list of public holidays for the specified country
    country_holidays = holidays.CountryHoliday(country)
    
    # Generate a date range and filter out weekends and public holidays
    business_days = pd.date_range(start=start_date, end=end_date, freq='B').tolist()
    business_days = [day for day in business_days if day not in country_holidays]
    
    return business_days