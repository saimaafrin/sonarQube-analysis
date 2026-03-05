import numpy as np
import itertools
def task_func(dimension, seed=42):
    # Set the seed for reproducibility
    np.random.seed(seed)
    
    # Create a 2D numpy array with random integers between 1 and 100
    matrix = np.random.randint(1, 101, size=dimension)
    
    # Flatten the matrix to a list
    flat_list = matrix.flatten().tolist()
    
    return (matrix, flat_list)
dimension = (3, 4)