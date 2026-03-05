import numpy as np
import pandas as pd
from dateutil.parser import parse
def task_func(dates_str_list):
    """
    Analyze the weekday distribution in a list of date strings.
    Implemented by dateutil.parser.
    This function takes a list of date strings in "yyyy-mm-dd" format, calculates the weekday for each date, and returns a distribution of the weekdays.
    The function should output with:
        Series: A pandas Series of the weekday distribution, where the index represents
        the weekdays (from Monday to Sunday) and the values represent the counts
        of each weekday in the provided list.
    """
    # Parse the date strings using dateutil.parser
    dates = [parse(date_str) for date_str in dates_str_list]

    # Calculate the weekday for each date
    weekdays = [date.weekday() for date in dates]

    # Create a pandas Series with the weekday distribution
    weekday_series = pd.Series(weekdays)

    # Reset the index of the Series to the weekdays
    weekday_series = weekday_series.reset_index(drop=True)

    # Return the weekday distribution
    return weekday_series
dates_str_list = ["2022-01-01", "2022-01-02", "2022-01-03", "2022-01-04", "2022-01-05", "2022-01-06", "2022-01-07"]