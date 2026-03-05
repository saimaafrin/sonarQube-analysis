
import pandas as pd
from datetime import datetime, timedelta
from random import randint, seed as random_seed

def task_func(start_date=datetime(2020, 1, 1), end_date=datetime(2020, 12, 31), seed=42):
    """
    Generates a pandas Series of random dates within a specified date range, including both start_date and end_date.
    
    Parameters:
    - start_date (datetime.datetime): The start date of the range. Must be a datetime.datetime instance.
    - end_date (datetime.datetime): The end date of the range. Must be a datetime.datetime instance.
    - seed (int): The seed for the random number generator for reproducibility. Default is 42.
    
    Returns:
    - pandas.Series: A Series object containing random dates within the specified range.
    
    Raises:
    - ValueError: If 'start_date' or 'end_date' is not a datetime.datetime instance, or if 'start_date' is later than 'end_date'.
    """
    if not isinstance(start_date, datetime) or not isinstance(end_date, datetime):
        raise ValueError("Both start_date and end_date must be datetime.datetime instances.")
    if start_date > end_date:
        raise ValueError("start_date must be earlier than or equal to end_date.")
    
    random_seed(seed)
    date_range = (end_date - start_date).days + 1
    random_dates = [start_date + timedelta(days=randint(0, date_range - 1)) for _ in range(date_range)]
    return pd.Series(random_dates, name='Random Dates')