import pandas as pd
import numpy as np
def task_func(data, key, min_value, max_value):
    """
    Add a new column with random values to the "data" DataFrame.
    The function should raise the exception for:
        The function will raise an error if the input data is not pandas DataFrame
    The function should output with:
        DataFrame: Updated DataFrame with the new column added.
    """
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input data must be a pandas DataFrame")

    # Generate random values for the new column
    new_values = np.random.randint(min_value, max_value, size=len(data))

    # Add the new column to the DataFrame
    data[key] = new_values

    return data
data = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
key = "C"
min_value = 0
max_value = 10