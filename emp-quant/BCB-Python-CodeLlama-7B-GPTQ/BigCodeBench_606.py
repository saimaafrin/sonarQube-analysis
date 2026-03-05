import pandas as pd
from scipy import stats
def task_func(matrix):
    """
    Normalizes a 2D numeric array (matrix) using the Z score.

    Args:
        matrix (numpy.ndarray): The input matrix.

    Returns:
        pandas.DataFrame: The normalized DataFrame.
    """
    # Calculate the mean and standard deviation of the input matrix
    mean = matrix.mean(axis=0)
    std = matrix.std(axis=0)

    # Calculate the Z scores for each row
    z_scores = (matrix - mean) / std

    # Create a DataFrame with the normalized data
    normalized_data = pd.DataFrame(z_scores, columns=matrix.columns)

    return normalized_data
matrix = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])