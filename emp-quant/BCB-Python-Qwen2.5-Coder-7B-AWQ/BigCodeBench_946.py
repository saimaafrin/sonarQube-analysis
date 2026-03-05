import numpy as np
import pandas as pd
import random
def task_func(rows=3, cols=2, min_val=0, max_val=100, seed=0):
    """
    Creates a matrix of specified dimensions with random integers within a given range, and then converts it into a pandas DataFrame.
    
    Parameters:
    rows (int): The number of rows in the matrix.
    cols (int): The number of columns in the matrix.
    min_val (int): The minimum value of the random integers.
    max_val (int): The maximum value of the random integers.
    seed (int): The seed for the random number generator.
    
    Returns:
    DataFrame: A pandas DataFrame containing random integers within the specified range.
    """
    # Set the seed for the random number generator
    random.seed(seed)
    
    # Create a matrix of random integers
    matrix = [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]
    
    # Convert the matrix to a pandas DataFrame
    df = pd.DataFrame(matrix)
    
    return df