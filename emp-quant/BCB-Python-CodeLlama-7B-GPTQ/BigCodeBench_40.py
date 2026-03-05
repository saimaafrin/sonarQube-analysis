import pandas as pd
import seaborn as sns
from scipy.stats import zscore
def task_func(data_matrix):
    # Calculate Z-values
    z_values = zscore(data_matrix, axis=0)

    # Calculate mean values
    mean_values = z_values.mean(axis=1)

    # Create DataFrame
    df = pd.DataFrame(z_values, columns=['Feature 1', 'Feature 2', ..., 'Feature n'])
    df['Mean'] = mean_values

    # Plot heatmap
    ax = sns.heatmap(df, annot=True, cmap='coolwarm')

    return df, ax
data_matrix = pd.DataFrame({'Feature 1': [1, 2, 3, 4, 5],
                           'Feature 2': [6, 7, 8, 9, 10],
                           'Feature 3': [11, 12, 13, 14, 15]})