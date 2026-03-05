
import pandas as pd
from datetime import datetime, timedelta
from random import randint, seed as random_seed

def task_func(start_date=datetime(2020, 1, 1), end_date=datetime(2020, 12, 31), seed=42):
    """
    Generate a pandas Series of random dates within a specified date range, including both start_date and end_date.
    
    Parameters:
    - start_date (datetime.datetime): The start date of the range (inclusive).
    - end_date (datetime.datetime): The end date of the range (inclusive).
    - seed (int): The seed for the random number generator for reproducibility.
    
    Returns:
    - pandas.Series: A Series object containing random dates within the specified range.
    
    Raises:
    - ValueError: If 'start_date' or 'end_date' is not a datetime.datetime instance, or if 'start_date' is later than 'end_date'.
    """
    # Validate input types
    if not isinstance(start_date, datetime) or not isinstance(end_date, datetime):
        raise ValueError("start_date and end_date must be datetime.datetime instances.")
    
    # Validate date range
    if start_date > end_date:
        raise ValueError("start_date must be earlier than or equal to end_date.")
    
    # Set the seed for reproducibility
    random_seed(seed)
    
    # Calculate the number of days in the range
    date_range = end_date - start_date + timedelta(days=1)
    num_days = date_range.days
    
    # Generate random dates
    random_dates = [start_date + timedelta(days=randint(0, num_days - 1)) for _ in range(num_days)]
    
    # Create a pandas Series from the list of random dates
    random_date_series = pd.Series(random_dates)
    
    return random_date_series