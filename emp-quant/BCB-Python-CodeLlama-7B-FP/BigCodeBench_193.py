import pandas as pd
import numpy as np
from random import choice
DATA_TYPES = [str, int, float, list, tuple, dict, set]
def task_func(rows, columns):
    """
    Generates a DataFrame with a specified number of rows and columns,
    populated with randomly generated data. Each column's data type is
    randomly selected from a set of Python data types, including primitive
    and complex structures.

    Args:
        rows (int): The number of rows in the DataFrame.
        columns (int): The number of columns in the DataFrame.

    Returns:
        pd.DataFrame: A DataFrame with the specified number of rows and
        columns named 'col0', 'col1', etc., containing randomly generated
        data.
    """
    # Initialize an empty list to store the data
    data = []

    # Generate random data for each column
    for i in range(columns):
        # Select a random data type from the list of supported data types
        data_type = choice(DATA_TYPES)

        # Generate random data based on the selected data type
        if data_type == str:
            data.append(np.random.choice(list('abcdefghij'), 5))
        elif data_type == int:
            data.append(np.random.randint(0, 10))
        elif data_type == float:
            data.append(np.random.uniform(0, 10))
        elif data_type == list:
            data.append(np.random.choice(list(range(10)), np.random.randint(1, 6)))
        elif data_type == tuple:
            data.append(tuple(np.random.choice(list(range(10)), np.random.randint(1, 6))))
        elif data_type == dict:
            data.append({np.random.randint(0, 10): np.random.randint(0, 10) for _ in range(np.random.randint(1, 6))})
        elif data_type == set:
            data.append(set(np.random.choice(list(range(10)), np.random.randint(1, 6))))

    # Create a DataFrame with the generated data
    df = pd.DataFrame(data, columns=['col{}'.format(i) for i in range(columns)])

    return df
rows = 10
columns = 5