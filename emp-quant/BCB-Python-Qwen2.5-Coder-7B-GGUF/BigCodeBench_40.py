
import pandas as pd
import seaborn as sns
from scipy.stats import zscore
import matplotlib.pyplot as plt

def task_func(data_matrix):
    # Calculate Z-scores for each row
    z_scores = pd.DataFrame(zscore(data_matrix, axis=1), columns=[f'Feature {i+1}' for i in range(data_matrix.shape[1])])
    
    # Calculate the mean of Z-scores per row
    z_scores['Mean'] = z_scores.mean(axis=1)
    
    # Calculate the correlation matrix of the Z-scores
    correlation_matrix = z_scores.corr()
    
    # Visualize the correlation matrix with a heatmap
    plt.figure(figsize=(10, 8))
    heatmap = sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Correlation Matrix of Z-scores')
    plt.show()
    
    return z_scores, heatmap