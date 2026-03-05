import numpy as np
from sklearn.preprocessing import MinMaxScaler
def task_func(rows=3, columns=2, seed=42):
    """
    Generate a matrix of random values with specified dimensions and scale it between 0 and 1.

    Parameters
    ----------
    rows : int, optional
        Number of rows in the matrix.
    columns : int, optional
        Number of columns in the matrix.
    seed : int, optional
        Random seed for reproducibility.

    Returns
    -------
    ndarray
        A numpy ndarray with scaled values between 0 and 1.
    """
    # Generate a matrix of random values
    matrix = np.random.rand(rows, columns)

    # Scale the matrix between 0 and 1
    scaler = MinMaxScaler()
    scaled_matrix = scaler.fit_transform(matrix)

    return scaled_matrix