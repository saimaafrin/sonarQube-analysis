
import numpy as np
import pandas as pd
from dateutil.parser import parse

def task_func(dates_str_list):
    dates = [parse(date_str) for date_str in dates_str_list]
    weekdays = [date.weekday() for date in dates]
    weekday_counts = np.bincount(weekdays)
    return pd.Series(weekday_counts, index=pd.Index(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], name="Weekday"))