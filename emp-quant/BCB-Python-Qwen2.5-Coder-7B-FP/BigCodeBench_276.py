import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
def task_func(matrix):
    # Calculate the maximum values of each row
    max_values = np.max(matrix, axis=1)
    
    # Calculate the histogram of the maximum values
    counts, bin_edges = np.histogram(max_values, bins='auto', density=True)
    
    # Calculate the core density estimate using Scott's rule
    bin_width = bin_edges[1] - bin_edges[0]
    bandwidth = bin_width * (len(max_values) ** (-1/3))
    kernel = stats.gaussian_kde(max_values, bw_method=bandwidth)
    
    # Calculate the skewness and kurtosis of the distribution
    skewness = stats.skew(max_values)
    kurtosis = stats.kurtosis(max_values)
    
    # Plot the histogram
    fig, ax = plt.subplots()
    ax.bar(bin_edges[:-1], counts, width=bin_width, align='edge', edgecolor='black')
    
    # Plot the core density estimate
    x = np.linspace(min(max_values), max(max_values), 1000)
    ax.plot(x, kernel(x), 'r-', lw=2)
    
    return skewness, kurtosis, ax