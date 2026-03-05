
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(dataframe):
    # Check if the DataFrame is empty
    if dataframe.empty:
        raise ValueError("The input DataFrame is empty")

    # Check if any column is non-numeric
    if not dataframe.apply(lambda x: x.dtype == np.number).all():
        raise TypeError("The DataFrame contains non-numeric columns")

    # Check if the DataFrame has fewer than two columns
    if len(dataframe.columns) < 2:
        raise ValueError("The DataFrame has fewer than two columns")

    # Calculate the correlation matrix
    corr_matrix = dataframe.corr()

    # Find the pair of columns with the highest absolute correlation
    max_corr = corr_matrix.max().max()
    max_corr_cols = corr_matrix.columns[corr_matrix.max() == max_corr]

    # Plot the scatter plot
    fig, ax = plt.subplots()
    ax.scatter(dataframe[max_corr_cols[0]], dataframe[max_corr_cols[1]])
    ax.set_xlabel(max_corr_cols[0])
    ax.set_ylabel(max_corr_cols[1])
    ax.set_title(f"Scatter Plot of {max_corr_cols[0]} and {max_corr_cols[1]}")

    return ax