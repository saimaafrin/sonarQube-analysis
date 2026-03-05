
import pandas as pd
import numpy as np
from random import choice, randint

# Constants
DATA_TYPES = [str, int, float, list, tuple, dict, set]

def task_func(rows, columns):
    """
    Generates a DataFrame with a specified number of rows and columns, populated with randomly generated data.
    Each column's data type is randomly selected from a set of Python data types, including primitive and complex structures.
    
    :param rows: int, the number of rows in the DataFrame
    :param columns: int, the number of columns in the DataFrame
    :return: pd.DataFrame, a DataFrame with the specified number of rows and columns
    """
    # Initialize an empty DataFrame
    df = pd.DataFrame()
    
    # Populate the DataFrame with data
    for _ in range(rows):
        row = []
        for _ in range(columns):
            data_type = choice(DATA_TYPES)
            if data_type == str:
                row.append(''.join([chr(randint(97, 122)) for _ in range(5)]))
            elif data_type == int:
                row.append(randint(0, 9))
            elif data_type == float:
                row.append(randint(0, 9) / 10.0)
            elif data_type == list:
                length = randint(1, 5)
                row.append([randint(0, 9) for _ in range(length)])
            elif data_type == tuple:
                length = randint(1, 5)
                row.append(tuple([randint(0, 9) for _ in range(length)]))
            elif data_type == dict:
                length = randint(1, 5)
                row.append({randint(0, 9): randint(0, 9) for _ in range(length)})
            elif data_type == set:
                length = randint(1, 5)
                row.append(set([randint(0, 9) for _ in range(length)]))
        df = df.append(pd.Series(row), ignore_index=True)
    
    return df