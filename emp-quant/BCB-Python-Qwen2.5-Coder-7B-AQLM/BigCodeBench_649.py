
import numpy as np
import pandas as pd
from dateutil.parser import parse

def task_func(dates_str_list):
    # Convert the list of date strings to a pandas Series
    dates_series = pd.Series(dates_str_list)
    
    # Parse the date strings into datetime objects
    parsed_dates = dates_series.apply(parse)
    
    # Extract the weekday from each datetime object
    weekdays = parsed_dates.dt.day_name()
    
    # Create a Series with the weekday distribution
    weekday_distribution = weekdays.value_counts().sort_index()
    
    return weekday_distribution