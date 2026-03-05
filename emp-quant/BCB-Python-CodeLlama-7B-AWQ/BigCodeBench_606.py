import pandas as pd
from scipy import stats
def task_func(matrix):
    """
    Normalizes a 2D numeric array (matrix) using the Z score.
    """
    # Calculate the mean and standard deviation of the matrix
    mean = matrix.mean(axis=0)
    std = matrix.std(axis=0)

    # Normalize the matrix using the Z score
    normalized_matrix = (matrix - mean) / std

    # Create a DataFrame from the normalized matrix
    normalized_df = pd.DataFrame(normalized_matrix)

    return normalized_df
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]