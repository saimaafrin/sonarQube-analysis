import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
def task_func(matrix):
    # Calculate the maximum values of each row
    max_values = np.max(matrix, axis=1)
    
    # Calculate skewness and kurtosis of the distribution
    skewness = stats.skew(max_values)
    kurtosis = stats.kurtosis(max_values)
    
    # Plot the histogram of the distribution
    fig, ax = plt.subplots()
    ax.hist(max_values, bins=30, density=True, alpha=0.6, color='g')
    
    # Return the skewness, kurtosis, and the histogram plot
    return skewness, kurtosis, ax