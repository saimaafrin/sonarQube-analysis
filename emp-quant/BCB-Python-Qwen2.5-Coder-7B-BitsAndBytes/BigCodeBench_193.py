
import pandas as pd
import numpy as np
from random import choice, randint

# Constants
DATA_TYPES = [str, int, float, list, tuple, dict, set]

def generate_random_data(data_type):
    if data_type == str:
        return ''.join(choice('abcdefghijklmnopqrstuvwxyz') for _ in range(5))
    elif data_type == int:
        return randint(0, 9)
    elif data_type == float:
        return float(randint(0, 9))
    elif data_type == list:
        return [randint(0, 9) for _ in range(randint(1, 5))]
    elif data_type == tuple:
        return tuple([randint(0, 9) for _ in range(randint(1, 5))])
    elif data_type == dict:
        return {randint(0, 9): randint(0, 9) for _ in range(randint(1, 5))}
    elif data_type == set:
        return {randint(0, 9) for _ in range(randint(1, 5))}

def task_func(rows, columns):
    data = {}
    for col in range(columns):
        col_name = f'col{col}'
        data[col_name] = [generate_random_data(choice(DATA_TYPES)) for _ in range(rows)]
    return pd.DataFrame(data)