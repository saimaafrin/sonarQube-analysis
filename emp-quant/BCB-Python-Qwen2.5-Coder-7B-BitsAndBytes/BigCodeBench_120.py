
import pandas as pd
from datetime import datetime, timedelta
from random import randint, seed as random_seed

def task_func(start_date=datetime(2020, 1, 1), end_date=datetime(2020, 12, 31), seed=42):
    """
    Generate a pandas Series of random dates within a specified date range.

    Parameters:
    - start_date (datetime): The start date of the range (inclusive).
    - end_date (datetime): The end date of the range (inclusive).
    - seed (int): Seed for the random number generator for reproducibility.

    Returns:
    - pandas.Series: A Series object containing random dates within the specified range.

    Raises:
    - ValueError: If 'start_date' or 'end_date' is not a datetime.datetime instance,
      or if 'start_date' is later than 'end_date'.
    """
    # Validate input types
    if not isinstance(start_date, datetime) or not isinstance(end_date, datetime):
        raise ValueError("Both start_date and end_date must be datetime instances.")
    
    # Ensure start_date is not later than end_date
    if start_date > end_date:
        raise ValueError("start_date cannot be later than end_date.")
    
    # Set the seed for reproducibility
    random_seed(seed)
    
    # Calculate the number of days between start_date and end_date
    num_days = (end_date - start_date).days + 1
    
    # Generate random indices
    random_indices = [randint(0, num_days - 1) for _ in range(num_days)]
    
    # Create a Series of dates using the random indices
    random_dates = pd.to_datetime([start_date + timedelta(days=i) for i in random_indices])
    
    return random_dates