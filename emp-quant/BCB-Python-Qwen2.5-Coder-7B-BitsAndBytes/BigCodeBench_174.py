
import pandas as pd
import numpy as np

def task_func(data, key, min_value, max_value):
    # Check if the input data is a pandas DataFrame
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input data must be a pandas DataFrame")
    
    # Generate random values and add them as a new column to the DataFrame
    data[key] = np.random.uniform(min_value, max_value, size=data.shape[0])
    
    return data