
import pandas as pd
import seaborn as sns
from scipy.stats import zscore

def task_func(data_matrix):
    # Calculate the Z-values for each row of the matrix
    z_scores = zscore(data_matrix, axis=0)

    # Calculate the mean value of each row
    mean_values = z_scores.mean(axis=1)

    # Create a DataFrame with the Z-scores and mean values
    df = pd.DataFrame(z_scores, columns=['Feature 1', 'Feature 2', ..., 'Feature n'])
    df['Mean'] = mean_values

    # Plot the heatmap of the correlation matrix
    ax = sns.heatmap(df, annot=True, cmap='viridis')

    return df, ax