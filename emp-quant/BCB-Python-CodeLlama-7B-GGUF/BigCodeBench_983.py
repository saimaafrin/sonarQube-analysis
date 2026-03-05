
import seaborn as sns
import numpy as np
import pandas as pd

def task_func(df):
    if df.empty:
        raise ValueError("DataFrame is empty")
    if not all(isinstance(x, (int, float)) for x in df.dtypes):
        raise TypeError("DataFrame contains non-numeric data types")

    covariance_df = df.cov()
    pair_plot = sns.pairplot(df)

    return covariance_df, pair_plot