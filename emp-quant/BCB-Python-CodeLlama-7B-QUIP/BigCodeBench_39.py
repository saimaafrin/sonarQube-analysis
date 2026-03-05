
import numpy as np
from scipy.stats import ttest_1samp
import matplotlib.pyplot as plt
# Constants
ALPHA = 0.05

def task_func(data_matrix):
    # Calculate the mean of each row in the data matrix
    means = np.mean(data_matrix, axis=1)

    # Run a t-test against the population mean for each mean
    t_values, p_values = ttest_1samp(means, data_matrix.mean(axis=0))

    # Determine which means are significantly different from the population mean
    significant_indices = np.where(p_values < ALPHA)[0]

    # Create a line plot with the means
    fig, ax = plt.subplots()
    ax.plot(means, label='Means')
    ax.set_xlabel('Mean')
    ax.set_ylabel('Value')

    # Create a line plot with the significant means
    ax2 = ax.twinx()
    ax2.plot(means[significant_indices], means[significant_indices], 'b', label='Significant Means')
    ax2.set_ylabel('Value')

    # Create a horizontal line representing the population mean
    ax3 = ax.twinx()
    ax3.axvline(data_matrix.mean(axis=0), color='g', label='Population Mean')
    ax3.set_xlabel('Mean')
    ax3.set_ylabel('Value')

    # Return the indices of the significant means
    return (significant_indices, ax)