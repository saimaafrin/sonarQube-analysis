
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(dataframe):
    # Check if the DataFrame is empty
    if dataframe.empty:
        raise ValueError("The input DataFrame is empty")

    # Check if any column is non-numeric
    if not all(dataframe.dtypes == 'float'):
        raise TypeError("The DataFrame contains non-numeric columns")

    # Calculate the correlation matrix
    corr_matrix = dataframe.corr()

    # Find the pair of columns with the highest absolute correlation
    abs_corr_matrix = np.abs(corr_matrix)
    max_corr_index = np.unravel_index(abs_corr_matrix.argmax(), abs_corr_matrix.shape)
    x_col = max_corr_index[0]
    y_col = max_corr_index[1]

    # Plot the scatter plot
    fig, ax = plt.subplots()
    ax.scatter(dataframe[x_col], dataframe[y_col])
    ax.set_xlabel(f"{x_col} column")
    ax.set_ylabel(f"{y_col} column")
    ax.set_title(f"Scatter plot of {x_col} and {y_col}")
    return ax