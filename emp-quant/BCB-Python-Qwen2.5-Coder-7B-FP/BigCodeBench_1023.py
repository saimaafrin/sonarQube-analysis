import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def task_func(dataframe):
    """
    Calculate the correlation matrix of a DataFrame and plot a scatter plot for the pair of columns with the highest absolute correlation.
    
    Parameters:
    - dataframe (pd.DataFrame): The input DataFrame.
    
    Returns:
    - ax (plt.Axes): The scatter plot of the pair of columns with the highest absolute correlation.
    
    Raises:
    - ValueError: If the input DataFrame is empty.
    - TypeError: If any column in the DataFrame is non-numeric.
    - ValueError: If the DataFrame has fewer than two columns.
    """
    # Check if the DataFrame is empty
    if dataframe.empty:
        raise ValueError("The input DataFrame is empty.")
    
    # Check if the DataFrame has fewer than two columns
    if dataframe.shape[1] < 2:
        raise ValueError("The DataFrame has fewer than two columns.")
    
    # Check if all columns are numeric
    if not np.issubdtype(dataframe.dtypes[0], np.number):
        raise TypeError("All columns in the DataFrame must be numeric.")
    
    # Calculate the correlation matrix
    corr_matrix = dataframe.corr()
    
    # Find the pair of columns with the highest absolute correlation
    max_corr = corr_matrix.abs().unstack().sort_values(kind="quicksort").drop_duplicates().idxmax()
    
    # Plot the scatter plot for the pair of columns with the highest absolute correlation
    ax = dataframe.plot.scatter(x=max_corr[0], y=max_corr[1])
    
    return ax