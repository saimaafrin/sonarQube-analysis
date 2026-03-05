import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import skew
def task_func(data_matrix):
    """
    Calculate the skew of each row in a 2D data matrix and plot the distribution.

    Parameters:
    data_matrix (pd.DataFrame): A 2D DataFrame containing the data.

    Returns:
    pd.DataFrame: A DataFrame containing the skewness of each row. The skewness is stored in a new column named 'Skewness'.
    matplotlib.axes.Axes: The Axes object of the plotted distribution.
    """
    # Calculate the skewness of each row
    data_matrix['Skewness'] = data_matrix.apply(lambda row: skew(row), axis=1)
    
    # Plot the distribution of skewness
    fig, ax = plt.subplots()
    ax.hist(data_matrix['Skewness'], bins=30, color='blue', alpha=0.7)
    ax.set_title('Distribution of Row Skewness')
    ax.set_xlabel('Skewness')
    ax.set_ylabel('Frequency')
    
    return data_matrix, ax