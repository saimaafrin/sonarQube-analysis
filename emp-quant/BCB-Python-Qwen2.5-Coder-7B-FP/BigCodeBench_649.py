import numpy as np
import pandas as pd
from dateutil.parser import parse
def task_func(dates_str_list):
    # Convert the list of date strings to a pandas Series
    dates_series = pd.Series(dates_str_list)
    
    # Parse the dates and extract the weekday
    weekdays = dates_series.apply(lambda x: parse(x).weekday())
    
    # Map the weekday numbers to weekday names
    weekday_names = weekdays.map({0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'})
    
    # Create a Series with the weekday distribution
    weekday_distribution = weekday_names.value_counts().sort_index()
    
    return weekday_distribution