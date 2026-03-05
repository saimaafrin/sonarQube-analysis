import numpy as np
from scipy.stats import ttest_1samp
import matplotlib.pyplot as plt
ALPHA = 0.05
def task_func(data_matrix):
    # Calculate the mean value of each row in the data matrix
    means = np.mean(data_matrix, axis=1)

    # Run a t-test from a sample against the population value
    t_stat, p_value = ttest_1samp(means, np.mean(data_matrix))

    # Record the mean values that differ significantly
    significant_indices = np.where(p_value < ALPHA)[0]

    # Create a lineplot with the mean of rows in red
    ax = plt.plot(means, color='red', label='Means')

    # Create a line plot with the significant_indices on the x-axis and the corresponding means on the y-axis
    ax = plt.plot(significant_indices, means[significant_indices], color='blue', label='Significant Means')

    # Create an horizontal line which represents the mean computed on the whole 2D matrix
    ax = plt.axhline(y=np.mean(data_matrix), color='green', label='Population Mean')

    # Add labels and title to the plot
    ax.set_xlabel('Indices')
    ax.set_ylabel('Means')
    ax.set_title('Means and Significant Means')

    # Return the list of indices of the means that are significantly different from the population mean
    return significant_indices, ax