import numpy as np
import pandas as pd
import random
def task_func(rows=3, cols=2, min_val=0, max_val=100, seed=0):
    """
    Creates a matrix of specified dimensions with random integers within a given range, and then converts it into a pandas DataFrame.

    Args:
        rows (int): Number of rows in the matrix.
        cols (int): Number of columns in the matrix.
        min_val (int): Minimum value in the matrix.
        max_val (int): Maximum value in the matrix.
        seed (int): Random seed.

    Returns:
        DataFrame: A pandas DataFrame containing random integers within the specified range.
    """
    # Generate a matrix with random integers within the specified range
    matrix = np.random.randint(min_val, max_val, size=(rows, cols), dtype=np.int64)

    # Convert the matrix to a pandas DataFrame
    df = pd.DataFrame(matrix)

    # Set the index and columns of the DataFrame
    df.index = range(rows)
    df.columns = range(cols)

    return df
rows = 3
cols = 2
min_val = 0
max_val = 100
seed = 0
matrix = np.random.randint(min_val, max_val, size=(rows, cols), dtype=np.int64)
df = pd.DataFrame(matrix)