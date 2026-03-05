
import seaborn as sns
import numpy as np
def task_func(df):
    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("The DataFrame is empty")

    # Check if the DataFrame contains non-numeric data types
    if not np.issubdtype(df.dtypes, np.number):
        raise TypeError("The DataFrame contains non-numeric data types")

    # Calculate the covariance matrix
    covariance_df = df.cov()

    # Create a pair plot
    pair_plot = sns.heatmap(covariance_df, annot=True, cmap="viridis")

    return covariance_df, pair_plot