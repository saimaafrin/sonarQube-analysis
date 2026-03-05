import numpy as np
from sklearn.preprocessing import MinMaxScaler
def task_func(rows=3, columns=2, seed=42):
    """
    Generate a matrix of random values with specified dimensions and scale it between 0 and 1.
    """
    np.random.seed(seed)
    matrix = np.random.rand(rows, columns)
    scaler = MinMaxScaler()
    scaled_matrix = scaler.fit_transform(matrix)
    return scaled_matrix