
import numpy as np
import random
from datetime import datetime

def task_func(rows=3, columns=2, start_date=datetime(2021, 1, 1), end_date=datetime(2021, 12, 31), seed=0):
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Calculate the total number of days between the start and end dates
    total_days = (end_date - start_date).days + 1
    
    # Generate a list of unique dates
    unique_dates = [start_date + datetime.timedelta(days=i) for i in range(total_days)]
    
    # Shuffle the list of unique dates
    random.shuffle(unique_dates)
    
    # Repeat the list of unique dates to fill the desired shape
    repeated_dates = unique_dates * (rows * columns)
    
    # Reshape the list to the desired shape
    matrix_of_dates = np.array(repeated_dates).reshape(rows, columns)
    
    return matrix_of_dates