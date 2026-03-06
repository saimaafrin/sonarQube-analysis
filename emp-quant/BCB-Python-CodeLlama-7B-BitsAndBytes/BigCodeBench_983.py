
import seaborn as sns
import numpy as np
import pandas as pd

def task_func(df):
    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("The DataFrame is empty.")

    # Check if the DataFrame contains non-numeric data types
    if not all(df.dtypes == np.number):
        raise TypeError("The DataFrame contains non-numeric data types.")

    # Calculate the covariance matrix
    covariance_df = df.cov()

    # Create a pair plot of the DataFrame
    pair_plot = sns.pairplot(df)

    return covariance_df, pair_plot