import pandas as pd
from datetime import datetime
import holidays
def task_func(start_date=datetime(2023, 1, 1), end_date=datetime(2023, 12, 31), country='US'):
    """
    Create a list of business days between two dates, excluding weekends and specified country's public holidays.

    Parameters:
    start_date (datetime): The start date. Default is January 1, 2023.
    end_date (datetime): The end date. Default is December 31, 2023. 
    country (str): ISO country code to determine public holidays. Default is 'US'.

    Returns:
    list[datetime]: A list of business days (as datetime objects). The start date and end date is included to process. 

    Raises:
    ValueError: If start_date is not a datetime object or is after end_date.
    ValueError: If end_date is not a datetime object or is before start_date.

    Requirements:
    - pandas
    - datetime
    - holidays

    Note:
    - The function depends on the 'holidays' package for fetching public holidays.
    - Ensure 'pandas' and 'holidays' packages are installed.

    Example:
    >>> business_days = task_func()
    >>> print(business_days[0])
    2023-01-03 00:00:00
    """
    if not isinstance(start_date, datetime):
        raise ValueError('start_date must be a datetime object.')
    if not isinstance(end_date, datetime):
        raise ValueError('end_date must be a datetime object.')
    if start_date > end_date:
        raise ValueError('start_date must be before end_date.')
    if end_date < start_date:
        raise ValueError('end_date must be after start_date.')

    # Create a list of business days between start_date and end_date
    business_days = []
    while start_date <= end_date:
        if start_date.weekday() not in [5, 6]:
            business_days.append(start_date)
        start_date += pd.Timedelta(days=1)

    # Remove public holidays
    holidays = holidays.CountryHoliday(country)
    business_days = [day for day in business_days if day not in holidays.values()]

    return business_days