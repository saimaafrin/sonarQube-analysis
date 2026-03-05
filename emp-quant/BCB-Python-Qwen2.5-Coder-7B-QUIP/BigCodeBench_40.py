
import pandas as pd
import seaborn as sns
from scipy.stats import zscore
import numpy as np
import matplotlib.pyplot as plt

def task_func(data_matrix):
    # Calculate Z-scores for each row
    z_scores = pd.DataFrame(zscore(data_matrix, axis=1), columns=[f'Feature {i+1}' for i in range(data_matrix.shape[1])])
    
    # Calculate the mean of Z-scores for each row
    z_scores['Mean'] = z_scores.mean(axis=1)
    
    # Calculate the correlation matrix of the Z-scores
    correlation_matrix = z_scores.corr()
    
    # Plot the heatmap of the correlation matrix
    plt.figure(figsize=(10, 8))
    heatmap = sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', cbar_kws={'format': '%.2f'})
    plt.title('Correlation Matrix of Z-scores')
    plt.show()
    
    return z_scores, heatmap