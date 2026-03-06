
import numpy as np
from scipy.linalg import svd

def task_func(rows=3, columns=2, seed=0):
    np.random.seed(seed)
    A = np.random.rand(rows, columns)
    U, s, Vh = svd(A, full_matrices=False)
    return U, s, Vh