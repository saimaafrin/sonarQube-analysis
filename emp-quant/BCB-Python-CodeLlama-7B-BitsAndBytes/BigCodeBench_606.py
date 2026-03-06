
import pandas as pd
from scipy import stats

def task_func(matrix):
    # Calculate the mean and standard deviation of each column
    means = matrix.mean(axis=0)
    stds = matrix.std(axis=0)

    # Calculate the Z scores for each column
    z_scores = (matrix - means) / stds

    # Create a new DataFrame with the normalized data
    normalized_data = pd.DataFrame(z_scores, columns=matrix.columns)

    return normalized_data