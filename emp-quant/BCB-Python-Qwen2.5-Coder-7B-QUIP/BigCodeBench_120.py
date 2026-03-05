
import pandas as pd
from datetime import datetime, timedelta
from random import randint, seed as random_seed

def task_func(start_date=datetime(2020, 1, 1), end_date=datetime(2020, 12, 31), seed=42):
    # Validate input dates
    if not isinstance(start_date, datetime) or not isinstance(end_date, datetime):
        raise ValueError("start_date and end_date must be datetime.datetime instances")
    if start_date > end_date:
        raise ValueError("start_date must be less than or equal to end_date")

    # Initialize random seed for reproducibility
    random_seed(seed)

    # Calculate the number of days in the range
    delta = end_date - start_date
    num_days = delta.days + 1

    # Generate random dates within the range
    random_dates = [start_date + timedelta(days=randint(0, delta.days)) for _ in range(num_days)]

    # Create a pandas Series from the list of random dates
    random_date_series = pd.Series(random_dates)

    return random_date_series