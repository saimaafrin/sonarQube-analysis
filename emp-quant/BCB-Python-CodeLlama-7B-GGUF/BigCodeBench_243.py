
import pandas as pd
import random

# Constants
N_DATA_POINTS = 10000
MIN_VALUE = 0.0
MAX_VALUE = 10.0

def task_func(n_data_points=N_DATA_POINTS):
    # Generate random floating-point numbers
    data = [random.uniform(MIN_VALUE, MAX_VALUE) for _ in range(n_data_points)]
    
    # Truncate to 3 decimal places
    data = [round(x, 3) for x in data]
    
    # Create a DataFrame
    df = pd.DataFrame({'Value': data})
    
    return df