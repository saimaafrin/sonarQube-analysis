
import numpy as np
import pandas as pd
from dateutil.parser import parse

def task_func(dates_str_list):
    # Convert the list of date strings to a list of datetime objects
    dates = [parse(date_str) for date_str in dates_str_list]
    
    # Extract the weekday from each datetime object
    weekdays = [date.weekday() for date in dates]
    
    # Map the weekday numbers to weekday names
    weekday_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    weekdays = [weekday_names[weekday] for weekday in weekdays]
    
    # Create a pandas Series to count the occurrences of each weekday
    weekday_distribution = pd.Series(weekdays).value_counts()
    
    return weekday_distribution