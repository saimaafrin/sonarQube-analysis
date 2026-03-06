
import numpy as np
import pandas as pd
from dateutil.parser import parse

def task_func(dates_str_list):
    # Parse the date strings using dateutil.parser
    dates = [parse(date_str) for date_str in dates_str_list]

    # Create a Series with the weekday distribution
    weekday_series = pd.Series(data=np.zeros(7), index=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

    # Iterate over the dates and increment the corresponding weekday in the Series
    for date in dates:
        weekday_series[date.weekday()] += 1

    return weekday_series