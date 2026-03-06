import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
def task_func(matrix):
    """
    Calculate the distribution of the maximum values of each row in the matrix, 
    record the histogram and the estimate of the core density of the distribution, 
    and return the skew, kurtosis, and the histogram plot of the distribution.
    
    Parameters:
    matrix (list): A list of lists representing a matrix.
    
    Returns:
    tuple: The skewness, the kurtosis of the distribution, and the histogram plot (matplotlib Axes object).
    
    Requirements:
    - numpy
    - scipy.stats
    - matplotlib.pyplot
    
    Example:
    >>> skew, kurtosis, ax = task_func([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    >>> round(skew, 2)
    0.0
    >>> round(kurtosis, 2)
    -1.5
    """
    # Calculate the distribution of the maximum values of each row in the matrix
    max_values = np.array([np.max(row) for row in matrix])
    # Record the histogram and the estimate of the core density of the distribution
    hist, bin_edges = np.histogram(max_values, bins=100)
    density = stats.kde.gaussian_kde(max_values)
    # Return the skew, kurtosis, and the histogram plot of the distribution
    return stats.skew(max_values), stats.kurtosis(max_values), density(bin_edges)