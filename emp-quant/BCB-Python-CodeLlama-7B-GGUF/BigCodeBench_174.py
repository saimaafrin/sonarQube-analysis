
import pandas as pd
import numpy as np

def task_func(data, key, min_value, max_value):
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input data must be a pandas DataFrame")

    # Add a new column with random values
    data[key] = np.random.randint(min_value, max_value, size=len(data))

    return data