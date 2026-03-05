
import numpy as np
import pandas as pd

# Constants
RANGE = (1, 100)

def task_func(L):
    """
    Generates a DataFrame filled with random integers.
    
    Parameters:
    L (list of lists of int): A list of lists where each sublist contains two integers.
    
    Returns:
    pandas.DataFrame: A DataFrame with random integers.
    """
    # Initialize an empty list to store the dimensions
    dimensions = []
    
    # Iterate through the list of lists to get the dimensions
    for pair in L:
        dimensions.extend(pair)
    
    # Ensure the dimensions list has exactly two elements
    if len(dimensions) != 2:
        raise ValueError("Each sublist in L must contain exactly two integers.")
    
    # Unpack the dimensions
    num_rows, num_cols = dimensions
    
    # Generate random integers using numpy
    random_data = np.random.randint(RANGE[0], RANGE[1], size=(num_rows, num_cols))
    
    # Create a DataFrame from the random data
    df = pd.DataFrame(random_data)
    
    return df