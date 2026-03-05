import pandas as pd
import seaborn as sns
from scipy.stats import zscore
def task_func(data_matrix):
    """
    Calculate the Z-values of a 2D data matrix, calculate the mean value of each row and then visualize the correlation matrix of the Z-values with a heatmap.
    The function should output with:
        tuple: A tuple containing:
            pandas.DataFrame: A DataFrame with columns 'Feature 1', 'Feature 2', ..., 'Feature n' containing the Z-scores (per matrix row).
            There is also an additional column 'Mean' the mean of z-score per row.
            matplotlib.axes.Axes: The Axes object of the plotted heatmap.
    """
    # Calculate Z-scores
    z_scores = zscore(data_matrix, axis=0)

    # Calculate mean values
    mean_values = z_scores.mean(axis=1)

    # Create DataFrame with Z-scores and mean values
    df = pd.DataFrame(z_scores, columns=['Feature 1', 'Feature 2', ..., 'Feature n'])
    df['Mean'] = mean_values

    # Plot heatmap
    ax = sns.heatmap(df, annot=True, cmap='coolwarm')

    return df, ax
data_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]