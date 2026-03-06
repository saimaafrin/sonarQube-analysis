
import seaborn as sns
import numpy as np
import pandas as pd

def task_func(df):
    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("The DataFrame is empty.")
    
    # Check if all columns in the DataFrame are numeric
    if not np.issubdtype(df.values.dtype, np.number):
        raise TypeError("The DataFrame contains non-numeric data types.")
    
    # Calculate the covariance matrix
    covariance_matrix = df.cov()
    covariance_df = pd.DataFrame(covariance_matrix)
    
    # Generate the pair plot
    pair_plot = sns.pairplot(df)
    
    return covariance_df, pair_plot