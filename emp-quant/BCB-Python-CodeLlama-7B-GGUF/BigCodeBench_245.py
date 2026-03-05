
import pandas as pd
import random
from scipy import stats

def task_func(n_data_points=5000, min_value=0.0, max_value=10.0):
    # Generate a random dataset of floating-point numbers within the specified range
    data = [random.uniform(min_value, max_value) for _ in range(n_data_points)]
    
    # Truncate each value to 3 decimal places
    data = [round(x, 3) for x in data]
    
    # Calculate statistical measures (mean, median, mode) of the data
    mean = stats.mean(data)
    median = stats.median(data)
    mode = stats.mode(data)
    
    # Return a dictionary with the calculated values
    return {'mean': mean, 'median': median, 'mode': mode}