
import pandas as pd
import numpy as np
from random import choice

# Constants
DATA_TYPES = [str, int, float, list, tuple, dict, set]

def task_func(rows, columns):
    # Create a list of random data types
    data_types = [choice(DATA_TYPES) for _ in range(columns)]

    # Create a list of random data
    data = [
        [np.random.randint(0, 10) for _ in range(rows)]
        for _ in range(columns)
    ]

    # Create a dictionary of column names and data types
    col_names = [f"col{i}" for i in range(columns)]
    col_types = dict(zip(col_names, data_types))

    # Create a DataFrame
    df = pd.DataFrame(data, columns=col_names, dtype=col_types)

    return df