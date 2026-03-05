import pandas as pd
import seaborn as sns
from scipy.stats import zscore
import numpy as np
def task_func(data_matrix):
    """
    Calculate the Z-values of a 2D data matrix, calculate the mean value of each row and then visualize the correlation matrix of the Z-values with a heatmap.
    """
    # Calculate Z-scores
    z_scores = zscore(data_matrix, axis=1)

    # Calculate mean of each row
    mean_values = z_scores.mean(axis=1)

    # Create DataFrame with Z-scores and mean values
    df = pd.DataFrame(z_scores, columns=['Feature 1', 'Feature 2', 'Feature 3', 'Feature 4'])
    df['Mean'] = mean_values

    # Plot heatmap
    ax = sns.heatmap(df.corr(), annot=True, cmap='coolwarm')

    return df, ax
data_matrix = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])