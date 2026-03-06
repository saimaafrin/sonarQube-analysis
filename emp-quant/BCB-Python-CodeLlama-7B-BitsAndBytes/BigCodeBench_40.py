
import pandas as pd
import seaborn as sns
from scipy.stats import zscore

def task_func(data_matrix):
    # Calculate Z-scores for each row of the data matrix
    z_scores = zscore(data_matrix, axis=1)

    # Calculate the mean value of each row
    mean_values = z_scores.mean(axis=1)

    # Create a DataFrame with the Z-scores and mean values
    df = pd.DataFrame(z_scores, columns=['Z-score'])
    df['Mean'] = mean_values

    # Plot the correlation matrix with a heatmap
    ax = sns.heatmap(df.corr(), annot=True, cmap='coolwarm')

    return df, ax