import numpy as np
import pandas as pd
from dateutil.parser import parse
def task_func(dates_str_list):
    """
    Analyze the weekday distribution in a list of date strings.

    Parameters
    ----------
    dates_str_list : list of str
        List of date strings in "yyyy-mm-dd" format.

    Returns
    -------
    Series
        A pandas Series of the weekday distribution, where the index represents
        the weekdays (from Monday to Sunday) and the values represent the counts
        of each weekday in the provided list.
    """
    # Convert the list of date strings to a list of datetime objects
    dates = [parse(date_str) for date_str in dates_str_list]

    # Calculate the weekday for each date
    weekdays = [date.weekday() for date in dates]

    # Create a pandas Series with the weekday distribution
    weekday_series = pd.Series(weekdays, index=pd.date_range('Monday', 'Sunday'))

    # Return the weekday distribution
    return weekday_series
dates_str_list = ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05', '2022-01-06', '2022-01-07']