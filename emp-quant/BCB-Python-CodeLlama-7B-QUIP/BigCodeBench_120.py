
import pandas as pd
from datetime import datetime, timedelta
from random import randint, seed as random_seed

def generate_random_dates(start_date, end_date, seed=42):
    if not isinstance(start_date, datetime):
        raise ValueError("'start_date' must be a datetime.datetime instance")
    if not isinstance(end_date, datetime):
        raise ValueError("'end_date' must be a datetime.datetime instance")
    if start_date > end_date:
        raise ValueError("'start_date' must be before or equal to 'end_date'")
    random_seed(seed)
    dates = []
    for i in range(timedelta(start_date, end_date).days + 1):
        dates.append(start_date + timedelta(days=randint(0, i)))
    return pd.Series(dates)