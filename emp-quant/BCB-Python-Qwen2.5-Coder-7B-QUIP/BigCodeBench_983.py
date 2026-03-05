
import seaborn as sns
import numpy as np
def task_func(df):
    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("DataFrame is empty")
    
    # Check if the DataFrame contains non-numeric data types
    if not df.select_dtypes(include=['number']).shape[1] == df.shape[1]:
        raise TypeError("DataFrame contains non-numeric data types")
    
    # Calculate the covariance matrix
    covariance_df = df.cov()
    
    # Create a pair plot
    pair_plot = sns.pairplot(df)
    
    return covariance_df, pair_plot