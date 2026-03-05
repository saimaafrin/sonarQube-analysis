import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import skew
def task_func(data_matrix):
    """
    Calculate the skew of each row in a 2D data matrix and plot the distribution.

    Parameters:
    data_matrix (pd.DataFrame): A 2D DataFrame containing the data.

    Returns:
    pd.DataFrame: A DataFrame containing the skewness of each row.
    matplotlib.axes.Axes: The Axes object of the plotted distribution.
    """
    # Calculate skewness for each row
    skewness_values = data_matrix.apply(skew, axis=1)
    
    # Create a DataFrame to store the skewness values
    result_df = pd.DataFrame(skewness_values, columns=['Skewness'])
    
    # Plot the distribution of skewness values
    fig, ax = plt.subplots()
    ax.hist(result_df['Skewness'], bins=30, edgecolor='k')
    ax.set_title('Distribution of Row Skewness')
    ax.set_xlabel('Skewness')
    ax.set_ylabel('Frequency')
    
    return result_df, ax