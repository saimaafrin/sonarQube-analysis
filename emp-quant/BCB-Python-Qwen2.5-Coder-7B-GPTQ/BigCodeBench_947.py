import numpy as np
import random
from datetime import datetime, timedelta
def task_func(rows=3, columns=2, start_date=datetime(2021, 1, 1), end_date=datetime(2021, 12, 31), seed=0):
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Calculate the number of days between the start and end date
    total_days = (end_date - start_date).days + 1
    
    # Generate unique random days within the range
    random_days = random.sample(range(total_days), rows * columns)
    
    # Convert the random days back to date objects
    dates = [start_date + timedelta(days=day) for day in random_days]
    
    # Reshape the list of dates into a numpy array
    date_array = np.array(dates).reshape(rows, columns)
    
    return date_array