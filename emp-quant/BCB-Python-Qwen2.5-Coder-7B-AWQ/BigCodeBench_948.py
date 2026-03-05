import numpy as np
from sklearn.preprocessing import MinMaxScaler
def task_func(rows=3, columns=2, seed=42):
    """
    Generate a matrix of random values with specified dimensions and scale it between 0 and 1.

    Parameters:
    rows (int): The number of rows in the matrix.
    columns (int): The number of columns in the matrix.
    seed (int): The seed for the random number generator for reproducibility.

    Returns:
    ndarray: A numpy ndarray with scaled values between 0 and 1.
    """
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Generate a matrix of random values
    random_matrix = np.random.rand(rows, columns)
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Scale the matrix between 0 and 1
    scaled_matrix = scaler.fit_transform(random_matrix)
    
    return scaled_matrix