
import pandas as pd
import numpy as np

def task_func(data, key, min_value, max_value):
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input data must be a pandas DataFrame")
    new_column = np.random.rand(len(data))
    data[key] = new_column
    return data