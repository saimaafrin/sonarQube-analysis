
import pandas as pd
import numpy as np
from random import choice

# Constants
DATA_TYPES = [str, int, float, list, tuple, dict, set]

def task_func(rows, columns):
    # Create a list of random data types for each column
    data_types = [choice(DATA_TYPES) for _ in range(columns)]

    # Create a list of random data for each column
    data = [np.random.randint(0, 10, size=rows) for _ in range(columns)]

    # Create a dictionary of column names and data types
    col_dict = {f'col{i}': data_types[i] for i in range(columns)}

    # Create a DataFrame with the specified number of rows and columns
    df = pd.DataFrame(data, columns=col_dict)

    return df