import pandas as pd
from datetime import datetime
import holidays
def task_func(start_date=datetime(2023, 1, 1), end_date=datetime(2023, 12, 31), country='US'):
    """
    Create a list of business days between two dates, excluding weekends and specified country's public holidays.

    Parameters
    ----------
    start_date : datetime
        The start date of the period to be processed.
    end_date : datetime
        The end date of the period to be processed.
    country : str
        The country for which public holidays are to be excluded.

    Returns
    -------
    list[datetime]
        A list of business days (as datetime objects). The start date and end date are included to process.

    Raises
    ------
    ValueError
        If start_date is not a datetime object or is after end_date.
    ValueError
        If end_date is not a datetime object or is before start_date.
    """
    if not isinstance(start_date, datetime):
        raise ValueError("start_date must be a datetime object")
    if not isinstance(end_date, datetime):
        raise ValueError("end_date must be a datetime object")
    if start_date > end_date:
        raise ValueError("start_date must be before end_date")
    if end_date < start_date:
        raise ValueError("end_date must be after start_date")

    # Create a list of all dates between start_date and end_date
    all_dates = pd.date_range(start_date, end_date)

    # Create a list of public holidays in the specified country
    country_holidays = holidays.CountryHoliday(country, years=range(start_date.year, end_date.year + 1))

    # Create a list of business days by excluding weekends and public holidays
    business_days = [date for date in all_dates if date.weekday() < 5 and date not in country_holidays]

    return business_days
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)
country = 'US'