
import numpy as np
from scipy.linalg import svd

def task_func(rows=3, columns=2, seed=0):
    np.random.seed(seed)
    matrix = np.random.rand(rows, columns)
    u, s, vh = svd(matrix, full_matrices=False)
    return u, s, vh