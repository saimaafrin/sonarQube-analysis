import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import skew
def task_func(data_matrix):
    """
    Calculate the skew of each row in a 2D data matrix and plot the distribution.
    The function should output with:
        pandas.DataFrame: A DataFrame containing the skewness of each row. The skweness is stored in a new column which name is 'Skewness'.
        matplotlib.axes.Axes: The Axes object of the plotted distribution.
    """
    # Calculate the skewness of each row
    skewness = data_matrix.apply(skew, axis=1)

    # Create a new DataFrame with the skewness
    skewness_df = pd.DataFrame(skewness, columns=['Skewness'])

    # Plot the distribution of the skewness
    ax = skewness_df['Skewness'].plot(kind='hist', bins=50)

    return skewness_df, ax
data_matrix = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])