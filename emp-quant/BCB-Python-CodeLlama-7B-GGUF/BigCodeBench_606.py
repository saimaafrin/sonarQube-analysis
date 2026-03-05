
import pandas as pd
from scipy import stats

def task_func(matrix):
    # Calculate the mean and standard deviation of each column
    means = matrix.mean(axis=0)
    stds = matrix.std(axis=0)

    # Calculate the Z scores for each column
    z_scores = (matrix - means) / stds

    # Normalize the Z scores to be between -1 and 1
    normalized_z_scores = (z_scores - z_scores.min()) / (z_scores.max() - z_scores.min())

    # Create a DataFrame with the normalized Z scores
    normalized_matrix = pd.DataFrame(normalized_z_scores, columns=matrix.columns)

    return normalized_matrix