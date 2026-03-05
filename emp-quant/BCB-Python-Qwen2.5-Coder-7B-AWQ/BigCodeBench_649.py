import numpy as np
import pandas as pd
from dateutil.parser import parse
def task_func(dates_str_list):
    """
    Analyzes the weekday distribution in a list of date strings.
    
    Parameters:
    dates_str_list (list): A list of date strings in "yyyy-mm-dd" format.
    
    Returns:
    Series: A pandas Series of the weekday distribution, where the index represents
    the weekdays (from Monday to Sunday) and the values represent the counts
    of each weekday in the provided list.
    """
    # Convert the list of date strings to a pandas Series
    dates_series = pd.Series(dates_str_list)
    
    # Parse the dates and extract the weekday
    weekdays = dates_series.apply(lambda x: parse(x).weekday())
    
    # Map the weekday numbers to weekday names
    weekday_names = weekdays.map({0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'})
    
    # Create a Series with the weekday distribution
    weekday_distribution = weekday_names.value_counts().sort_index()
    
    return weekday_distribution
dates_str_list = [
    "2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04", "2023-01-05",
    "2023-01-06", "2023-01-07", "2023-01-08", "2023-01-09", "2023-01-10",
    "2023-01-11", "2023-01-12", "2023-01-13", "2023-01-14", "2023-01-15",
    "2023-01-16", "2023-01-17", "2023-01-18", "2023-01-19", "2023-01-20",
    "2023-01-21", "2023-01-22", "2023-01-23", "2023-01-24", "2023-01-25",
    "2023-01-26", "2023-01-27", "2023-01-28", "2023-01-29", "2023-01-30",
    "2023-01-31"
]