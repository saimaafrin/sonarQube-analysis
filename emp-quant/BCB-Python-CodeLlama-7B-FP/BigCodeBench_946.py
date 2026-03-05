import numpy as np
import pandas as pd
import random
def task_func(rows=3, cols=2, min_val=0, max_val=100, seed=0):
    """
    Creates a matrix of specified dimensions with random integers within a given range, and then converts it into a pandas DataFrame.
    """
    # Set the random seed for reproducibility
    random.seed(seed)

    # Create a matrix of random integers within the specified range
    matrix = np.random.randint(min_val, max_val, size=(rows, cols))

    # Convert the matrix to a pandas DataFrame
    df = pd.DataFrame(matrix)

    # Return the DataFrame
    return df
rows = 3
cols = 2
min_val = 0
max_val = 100
seed = 0