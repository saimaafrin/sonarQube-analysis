
import numpy as np
import pandas as pd
from dateutil.parser import parse

def task_func(dates_str_list):
    # Parse the date strings to datetime objects
    dates = [parse(date_str) for date_str in dates_str_list]

    # Calculate the weekday for each date
    weekdays = [date.weekday() for date in dates]

    # Create a pandas Series with the weekday distribution
    weekday_series = pd.Series(weekdays, index=pd.Index(range(7), name='Weekday'))

    # Return the weekday distribution
    return weekday_series