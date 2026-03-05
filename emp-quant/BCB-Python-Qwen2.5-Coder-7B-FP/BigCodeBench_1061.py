import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
def task_func(arr: np.ndarray) -> (plt.Axes, np.ndarray):
    """
    Plots a histogram of normalized data from an input 2D numpy array alongside the probability density function (PDF) of a standard normal distribution.
    
    Parameters:
    arr (np.ndarray): A 2D numpy array as input.
    
    Returns:
    tuple: A matplotlib Axes object with the histogram of the normalized data and the overlaid standard normal PDF, and the normalized data as a 1D numpy array.
    """
    # Calculate the sum of elements in each row
    row_sums = np.sum(arr, axis=1)
    
    # Calculate mean and standard deviation of the row sums
    mean = np.mean(row_sums)
    std_dev = np.std(row_sums)
    
    # Normalize the row sums
    if std_dev == 0:
        normalized_data = np.zeros_like(row_sums)
    else:
        normalized_data = (row_sums - mean) / std_dev
    
    # Plot histogram of the normalized data
    fig, ax = plt.subplots()
    ax.hist(normalized_data, bins=30, density=True, alpha=0.6, color='green')
    
    # Plot the PDF of a standard normal distribution
    x = np.linspace(norm.ppf(0.005), norm.ppf(0.995), 100)
    ax.plot(x, norm.pdf(x), 'r-', lw=2)
    
    # Set the title of the plot
    ax.set_title('Histogram of Normalized Data with Standard Normal PDF')
    
    return ax, normalized_data