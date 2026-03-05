
import numpy as np
import pandas as pd

# Constants
RANGE = (1, 100)

def task_func(L):
    """
    Generates a DataFrame filled with random integers. The dimensions of the DataFrame
    (number of rows and columns) are determined by multiplying pairs of integers from nested lists
    within the input list of lists 'L'.
    
    Parameters:
    L (list of list of int): A list of lists containing pairs of integers.
    
    Returns:
    DataFrame: A pandas DataFrame with random integers.
    """
    # Initialize an empty list to store the dimensions
    dimensions = []
    
    # Iterate through the nested lists and multiply the pairs to get the dimensions
    for pair in L:
        if len(pair) == 2:
            dimensions.append(pair[0] * pair[1])
        else:
            raise ValueError("Each sublist must contain exactly two integers.")
    
    # Ensure the dimensions list has exactly two elements
    if len(dimensions) != 2:
        raise ValueError("The input list must contain exactly two sublists.")
    
    # Generate a DataFrame with random integers
    df = pd.DataFrame(np.random.randint(RANGE[0], RANGE[1], size=(dimensions[0], dimensions[1])))
    
    return df