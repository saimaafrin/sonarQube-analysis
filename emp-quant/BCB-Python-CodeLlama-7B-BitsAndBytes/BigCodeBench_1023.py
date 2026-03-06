
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(dataframe):
    # Check if the input DataFrame is empty
    if dataframe.empty:
        raise ValueError("Input DataFrame is empty")

    # Check if any column in the DataFrame is non-numeric
    if not all(dataframe.dtypes == np.number):
        raise TypeError("Non-numeric column in DataFrame")

    # Check if the DataFrame has fewer than two columns
    if len(dataframe.columns) < 2:
        raise ValueError("DataFrame has fewer than two columns")

    # Calculate the correlation matrix
    corr_matrix = dataframe.corr()

    # Find the pair of columns with the highest absolute correlation
    max_corr = np.max(np.abs(corr_matrix))
    max_corr_col1, max_corr_col2 = np.where(np.abs(corr_matrix) == max_corr)
    max_corr_col1 = max_corr_col1[0]
    max_corr_col2 = max_corr_col2[0]

    # Plot the scatter plot
    ax = plt.scatter(dataframe[max_corr_col1], dataframe[max_corr_col2])

    return ax