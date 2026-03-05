
import numpy as np
from scipy.linalg import svd

def task_func(rows=3, columns=2, seed=0):
    """
    Generates a matrix of random values with specified dimensions and performs Singular Value Decomposition (SVD) on it.
    
    Parameters:
    rows (int): The number of rows in the matrix.
    columns (int): The number of columns in the matrix.
    seed (int): The seed for the random number generator for reproducibility.
    
    Returns:
    tuple: A tuple containing three elements:
        U (ndarray): The unitary matrix U.
        s (ndarray): The singular values, sorted in descending order.
        Vh (ndarray): The conjugate transpose of the unitary matrix V.
    """
    # Set the seed for the random number generator
    np.random.seed(seed)
    
    # Generate a random matrix
    matrix = np.random.rand(rows, columns)
    
    # Perform Singular Value Decomposition
    U, s, Vh = svd(matrix)
    
    return U, s, Vh