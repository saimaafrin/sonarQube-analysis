
import numpy as np
import itertools

def task_func(dimension, seed=42):
    # Set the seed for reproducibility
    np.random.seed(seed)
    
    # Create a 2D numpy array of the given dimension with random integers between 1 and 100
    matrix = np.random.randint(1, 101, size=dimension)
    
    # Flatten the matrix to get a list of all elements
    flat_list = matrix.flatten().tolist()
    
    return matrix, flat_list