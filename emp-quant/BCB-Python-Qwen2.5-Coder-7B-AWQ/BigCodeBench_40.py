import pandas as pd
import seaborn as sns
from scipy.stats import zscore
import matplotlib.pyplot as plt
def task_func(data_matrix):
    """
    Calculate the Z-values of a 2D data matrix, calculate the mean value of each row and then visualize the correlation matrix of the Z-values with a heatmap.
    
    Parameters:
    data_matrix (np.ndarray): A 2D numpy array containing the data.
    
    Returns:
    tuple: A tuple containing:
        pandas.DataFrame: A DataFrame with columns 'Feature 1', 'Feature 2', ..., 'Feature n' containing the Z-scores (per matrix row).
        There is also an additional column 'Mean' the mean of z-score per row.
        matplotlib.axes.Axes: The Axes object of the plotted heatmap.
    """
    # Calculate Z-scores for each row
    z_scores = pd.DataFrame(zscore(data_matrix, axis=1), columns=[f'Feature {i+1}' for i in range(data_matrix.shape[1])])
    
    # Calculate the mean of Z-scores per row
    z_scores['Mean'] = z_scores.mean(axis=1)
    
    # Calculate the correlation matrix of Z-scores
    correlation_matrix = z_scores.corr()
    
    # Plot the heatmap of the correlation matrix
    plt.figure(figsize=(10, 8))
    heatmap = sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Correlation Matrix of Z-Scores')
    plt.show()
    
    return z_scores, heatmap