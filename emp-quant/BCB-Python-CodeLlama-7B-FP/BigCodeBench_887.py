import pandas as pd
import numpy as np
import itertools
def task_func(T1, row_num=50, seed=None):
    """
    Convert elements in 'T1' to integers and create a Pandas DataFrame with random numbers.
    The number of columns in the DataFrame is determined by the sum of the integers in 'T1',
    and the number of rows is defined by the 'row_num' parameter.
    """
    # Convert elements in 'T1' to integers
    T1_int = [int(x) for x in T1]

    # Determine the number of columns in the DataFrame
    num_cols = sum(T1_int)

    # Create a list of random numbers for each column
    col_list = [np.random.randint(0, 100, size=row_num) for _ in range(num_cols)]

    # Create a list of column names
    col_names = [f"Col_{i}" for i in range(1, num_cols + 1)]

    # Create a Pandas DataFrame
    df = pd.DataFrame(col_list, columns=col_names)

    return df
T1 = (('1', '12'), ('1', '-12'))