
import pandas as pd
import numpy as np

def task_func(data, key, min_value, max_value):
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input data must be a pandas DataFrame")
    
    data[key] = np.random.uniform(min_value, max_value, size=len(data))
    
    return data