
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
    skewness = data_matrix.apply(skew, axis=1)
    
    # Create a DataFrame to store the skewness
    skewness_df = pd.DataFrame(skewness, columns=['Skewness'])
    
    # Plot the distribution of skewness
    fig, ax = plt.subplots()
    skewness_df['Skewness'].hist(ax=ax, bins=20, color='blue', edgecolor='black')
    ax.set_title('Distribution of Row Skewness')
    ax.set_xlabel('Skewness')
    ax.set_ylabel('Frequency')
    
    return skewness_df, ax