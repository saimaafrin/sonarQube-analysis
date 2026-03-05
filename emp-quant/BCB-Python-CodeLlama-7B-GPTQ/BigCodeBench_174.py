import pandas as pd
import numpy as np
def task_func(data, key, min_value, max_value):
    """
    Add a new column with random values to the "data" DataFrame.

    Args:
        data (pandas.DataFrame): Input DataFrame.
        key (str): Name of the new column.
        min_value (int): Minimum value for the new column.
        max_value (int): Maximum value for the new column.

    Returns:
        pandas.DataFrame: Updated DataFrame with the new column added.

    Raises:
        TypeError: If the input data is not a pandas DataFrame.
    """
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Input data must be a pandas DataFrame.")

    # Generate random values for the new column
    values = np.random.randint(min_value, max_value, size=len(data))

    # Add the new column to the DataFrame
    data[key] = values

    return data
data = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [6, 7, 8, 9, 10]})