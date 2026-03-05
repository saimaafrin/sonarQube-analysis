import pandas as pd
import numpy as np
from random import choice, randint
DATA_TYPES = [str, int, float, list, tuple, dict, set]
def task_func(rows, columns):
    """
    Generates a DataFrame with a specified number of rows and columns, populated with randomly generated data.
    
    Parameters:
    rows (int): The number of rows in the DataFrame.
    columns (int): The number of columns in the DataFrame.
    
    Returns:
    pd.DataFrame: A DataFrame with the specified number of rows and columns named 'col0', 'col1', etc.,
                 containing randomly generated data.
    """
    data = {}
    for col in range(columns):
        col_name = f'col{col}'
        data[col_name] = []
        for _ in range(rows):
            data_type = choice(DATA_TYPES)
            if data_type == str:
                value = ''.join(choice('abcdefghijklmnopqrstuvwxyz') for _ in range(5))
            elif data_type == int:
                value = randint(0, 9)
            elif data_type == float:
                value = float(randint(0, 9))
            elif data_type == list:
                value = [randint(0, 9) for _ in range(randint(1, 5))]
            elif data_type == tuple:
                value = tuple(randint(0, 9) for _ in range(randint(1, 5)))
            elif data_type == dict:
                value = {randint(0, 9): randint(0, 9) for _ in range(randint(1, 5))}
            elif data_type == set:
                value = set(randint(0, 9) for _ in range(randint(1, 5)))
            data[col_name].append(value)
    
    return pd.DataFrame(data)