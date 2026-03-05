
import pandas as pd
import numpy as np
from random import choice, randint

# Constants
DATA_TYPES = [str, int, float, list, tuple, dict, set]

def task_func(rows, columns):
    """
    Generates a DataFrame with a specified number of rows and columns, populated with randomly generated data.
    
    Parameters:
    rows (int): The number of rows in the DataFrame.
    columns (int): The number of columns in the DataFrame.
    
    Returns:
    pd.DataFrame: A DataFrame with the specified number of rows and columns named 'col0', 'col1', etc., containing randomly generated data.
    """
    data = {}
    for col in range(columns):
        column_name = f'col{col}'
        column_data = []
        for row in range(rows):
            data_type = choice(DATA_TYPES)
            if data_type == str:
                column_data.append(''.join(choice('abcdefghijklmnopqrstuvwxyz') for _ in range(5)))
            elif data_type == int:
                column_data.append(randint(0, 9))
            elif data_type == float:
                column_data.append(float(randint(0, 9)))
            elif data_type == list:
                column_data.append([randint(0, 9) for _ in range(randint(1, 5))])
            elif data_type == tuple:
                column_data.append(tuple(randint(0, 9) for _ in range(randint(1, 5))))
            elif data_type == dict:
                column_data.append({randint(0, 9): randint(0, 9) for _ in range(randint(1, 5))})
            elif data_type == set:
                column_data.append(set(randint(0, 9) for _ in range(randint(1, 5))))
        data[column_name] = column_data
    
    return pd.DataFrame(data)