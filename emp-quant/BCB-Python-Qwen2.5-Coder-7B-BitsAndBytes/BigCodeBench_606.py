
import pandas as pd
from scipy import stats

def task_func(matrix):
    """
    Normalizes a 2D numeric array (matrix) using the Z score.

    Parameters:
    matrix (list of lists): A 2D list representing the matrix to be normalized.

    Returns:
    DataFrame: The normalized DataFrame.
    """
    # Convert the matrix to a pandas DataFrame
    df = pd.DataFrame(matrix)
    
    # Apply the Z-score normalization
    normalized_df = df.apply(stats.zscore)
    
    return normalized_df