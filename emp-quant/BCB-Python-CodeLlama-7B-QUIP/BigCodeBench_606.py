
import pandas as pd
from scipy import stats

def task_func(matrix):
    # Normalize the matrix using the Z score
    z_scores = stats.zscore(matrix)
    # Create a DataFrame from the normalized matrix
    normalized_matrix = pd.DataFrame(z_scores, columns=matrix.columns, index=matrix.index)
    return normalized_matrix