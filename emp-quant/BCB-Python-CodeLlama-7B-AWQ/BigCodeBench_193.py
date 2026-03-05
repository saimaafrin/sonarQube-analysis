import pandas as pd
import numpy as np
from random import choice
DATA_TYPES = [str, int, float, list, tuple, dict, set]
def task_func(rows, columns):
    """
    Generates a DataFrame with a specified number of rows and columns, populated with randomly generated data.
    Each column's data type is randomly selected from a set of Python data types, including primitive and complex structures.
    DataFrame: A DataFrame in which each column's data type could be one of the following, with random content generated accordingly:
    - str: Random strings of 5 lowercase alphabetic characters.
    - int: Random integers from 0 to 9.
    - float: Random floats derived by converting integers from 0 to 9 into float.
    - list: Lists of random length (1 to 5) containing integers from 0 to 9.
    - tuple: Tuples of random length (1 to 5) containing integers from 0 to 9.
    - dict: Dictionaries with a random number (1 to 5) of key-value pairs, keys and values are integers from 0 to 9.
    - set: Sets of random size (1 to 5) containing unique integers from 0 to 9.
    """
    data = {}
    for i in range(columns):
        data[f'col{i}'] = []
        for j in range(rows):
            data[f'col{i}'].append(choice(DATA_TYPES)())
    return pd.DataFrame(data)