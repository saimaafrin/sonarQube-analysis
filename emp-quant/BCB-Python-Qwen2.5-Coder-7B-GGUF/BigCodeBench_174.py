
import pandas as pd
import numpy as np

def task_func(data, key, min_value, max_value):
    if not isinstance(data, pd.DataFrame):
        raise ValueError("The input data must be a pandas DataFrame")
    
    data[key] = np.random.uniform(min_value, max_value, size=data.shape[0])
    return data