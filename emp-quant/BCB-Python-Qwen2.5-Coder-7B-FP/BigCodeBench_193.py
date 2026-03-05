import pandas as pd
import numpy as np
from random import choice, randint, uniform, sample
DATA_TYPES = [str, int, float, list, tuple, dict, set]
def task_func(rows, columns):
    """
    Generates a DataFrame with specified number of rows and columns, populated with randomly generated data.
    
    Parameters:
    rows (int): The number of rows in the DataFrame.
    columns (int): The number of columns in the DataFrame.
    
    Returns:
    pd.DataFrame: A DataFrame with the specified number of rows and columns containing randomly generated data.
    """
    data = {}
    for col in range(columns):
        col_name = f'col{col}'
        data[col_name] = []
        for _ in range(rows):
            data_type = choice(DATA_TYPES)
            if data_type == str:
                data[col_name].append(''.join(choice('abcdefghijklmnopqrstuvwxyz') for _ in range(5)))
            elif data_type == int:
                data[col_name].append(randint(0, 9))
            elif data_type == float:
                data[col_name].append(uniform(0, 9))
            elif data_type == list:
                data[col_name].append(sample(range(10), randint(1, 5)))
            elif data_type == tuple:
                data[col_name].append(tuple(sample(range(10), randint(1, 5))))
            elif data_type == dict:
                data[col_name].append(dict(zip(sample(range(10), randint(1, 5)), sample(range(10), randint(1, 5)))))
            elif data_type == set:
                data[col_name].append(set(sample(range(10), randint(1, 5))))
    
    return pd.DataFrame(data)