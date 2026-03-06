
import numpy as np
from scipy.linalg import svd

def task_func(rows=3, columns=2, seed=0):
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Generate a random matrix with the specified dimensions
    matrix = np.random.rand(rows, columns)
    
    # Perform Singular Value Decomposition
    U, s, Vh = svd(matrix, full_matrices=False)
    
    return U, s, Vh