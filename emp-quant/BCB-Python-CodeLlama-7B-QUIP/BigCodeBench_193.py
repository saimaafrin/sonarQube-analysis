
import pandas as pd
import numpy as np
from random import choice
# Constants
DATA_TYPES = [str, int, float, list, tuple, dict, set]
def task_func(rows, columns):
    # Create a list of random data for each column
    data = [choice(DATA_TYPES) for i in range(columns)]
    # Create a DataFrame with the specified number of rows and columns
    df = pd.DataFrame(data, columns=['col' + str(i) for i in range(columns)])
    return df