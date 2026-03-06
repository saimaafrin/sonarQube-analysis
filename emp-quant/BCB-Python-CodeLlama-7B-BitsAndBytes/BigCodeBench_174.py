
import pandas as pd
import numpy as np

def task_func(data, key, min_value, max_value):
    # Check if the input is a pandas DataFrame
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input data must be a pandas DataFrame")

    # Generate random values for the new column
    new_values = np.random.uniform(min_value, max_value, size=len(data))

    # Add the new column to the DataFrame
    data[key] = new_values

    # Return the updated DataFrame
    return data