
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def task_func(matrix):
    # Calculate the maximum values of each row
    row_max_values = np.max(matrix, axis=1)
    
    # Calculate the histogram of the row max values
    counts, bin_edges = np.histogram(row_max_values, bins=10, density=True)
    
    # Estimate the core density of the distribution
    core_density = stats.gaussian_kde(row_max_values)
    
    # Calculate skewness and kurtosis
    skewness = stats.skew(row_max_values)
    kurtosis = stats.kurtosis(row_max_values)
    
    # Plot the histogram
    plt.figure()
    plt.hist(row_max_values, bins=10, density=True, alpha=0.6)
    plt.title('Histogram of Row Max Values')
    plt.xlabel('Value')
    plt.ylabel('Density')
    
    # Return the skewness, kurtosis, and the histogram plot
    return skewness, kurtosis, plt.gca()