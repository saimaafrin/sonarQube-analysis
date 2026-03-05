
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def task_func(matrix):
    # Calculate the maximum values of each row
    max_values = np.max(matrix, axis=1)
    
    # Calculate the histogram of the maximum values
    hist, bin_edges = np.histogram(max_values, bins=30, density=True)
    
    # Estimate the core density of the distribution
    core_density = np.max(hist)
    
    # Calculate skewness and kurtosis
    skewness = stats.skew(max_values)
    kurtosis = stats.kurtosis(max_values)
    
    # Plot the histogram
    fig, ax = plt.subplots()
    ax.bar(bin_edges[:-1], hist, width=np.diff(bin_edges), edgecolor='black')
    ax.set_title('Histogram of Maximum Values')
    ax.set_xlabel('Maximum Value')
    ax.set_ylabel('Density')
    
    # Return the skewness, kurtosis, and the histogram plot
    return skewness, kurtosis, ax