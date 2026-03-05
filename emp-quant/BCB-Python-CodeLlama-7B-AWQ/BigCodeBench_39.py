import numpy as np
from scipy.stats import ttest_1samp
import matplotlib.pyplot as plt
ALPHA = 0.05
def task_func(data_matrix):
    """
    Calculate the mean value of each row in a 2D data matrix, run a t-test from a sample against the population value, and record the mean values that differ significantly.
    """
    # Calculate the mean of each row
    row_means = np.mean(data_matrix, axis=1)

    # Run t-test for each row
    t_stats, p_values = ttest_1samp(data_matrix, popmean=row_means)

    # Identify significant means
    significant_indices = np.where(p_values < ALPHA)[0]

    # Plot the means and significant means
    fig, ax = plt.subplots()
    ax.plot(row_means, label='Means')
    ax.plot(significant_indices, row_means[significant_indices], 'bo', label='Significant Means')
    ax.axhline(row_means.mean(), color='g', label='Population Mean')
    ax.legend()

    return significant_indices, ax