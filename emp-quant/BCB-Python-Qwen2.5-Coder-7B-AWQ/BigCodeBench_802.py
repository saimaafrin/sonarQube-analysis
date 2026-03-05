import numpy as np
import itertools
def task_func(dimension, seed=42):
    """
    Generates a 2D numpy array of a given dimension with random integers between 1 and 100,
    and a flat list of all elements in the matrix.
    
    Parameters:
    - dimension: A tuple (rows, cols) representing the dimensions of the matrix.
    - seed: An integer used as the seed for the random number generator for reproducibility.
    
    Returns:
    - A tuple containing:
        - A 2D numpy array of the given dimension with random integers between 1 and 100.
        - A flat list of all elements in the matrix.
    """
    # Set the seed for the random number generator
    np.random.seed(seed)
    
    # Generate the 2D numpy array with random integers between 1 and 100
    matrix = np.random.randint(1, 101, size=dimension)
    
    # Flatten the matrix to a list
    flat_list = matrix.flatten().tolist()
    
    return matrix, flat_list