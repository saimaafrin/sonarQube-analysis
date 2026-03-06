
import pandas as pd
import seaborn as sns
from scipy.stats import zscore
import matplotlib.pyplot as plt

def task_func(data_matrix):
    # Calculate Z-scores for each row
    z_scores = data_matrix.apply(zscore, axis=1)
    
    # Add a new column for the mean of Z-scores per row
    z_scores['Mean'] = z_scores.mean(axis=1)
    
    # Compute the correlation matrix of the Z-scores
    corr_matrix = z_scores.corr()
    
    # Create a heatmap to visualize the correlation matrix
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5, ax=ax)
    plt.title('Correlation Matrix of Z-Scores')
    plt.show()
    
    return z_scores, ax

    result_df, heatmap_ax = task_func(data_matrix)
    print(result_df)