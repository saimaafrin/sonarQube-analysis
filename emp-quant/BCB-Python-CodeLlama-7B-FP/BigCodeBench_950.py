import numpy as np
from scipy.linalg import svd
def task_func(rows=3, columns=2, seed=0):
    """
    Generate a matrix of random values with specified dimensions and perform Singular Value Decomposition (SVD) on it.
    The function should output with:
        tuple: A tuple containing three elements:
        U (ndarray): The unitary matrix U.
        s (ndarray): The singular values, sorted in descending order.
        Vh (ndarray): The conjugate transpose of the unitary matrix V.
    """
    np.random.seed(seed)
    A = np.random.rand(rows, columns)
    U, s, Vh = svd(A)
    return U, s, Vh