import numpy as np
import pandas as pd
from dateutil.parser import parse
def task_func(dates_str_list):
    """
    Analyze the weekday distribution in a list of date strings.

    Parameters
    ----------
    dates_str_list : list of str
        A list of date strings in "yyyy-mm-dd" format.

    Returns
    -------
    Series : pandas.Series
        A pandas Series of the weekday distribution, where the index represents
        the weekdays (from Monday to Sunday) and the values represent the counts
        of each weekday in the provided list.
    """
    # Convert the date strings to datetime objects
    dates = [parse(date_str) for date_str in dates_str_list]

    # Create a Series with the weekday as the index and the count as the value
    weekday_counts = pd.Series(data=np.zeros(7), index=pd.date_range(start='2022-01-01', end='2022-01-07', freq='D'))
    for date in dates:
        weekday_counts.loc[date.weekday()] += 1

    return weekday_counts
dates_str_list = ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05', '2022-01-06', '2022-01-07']