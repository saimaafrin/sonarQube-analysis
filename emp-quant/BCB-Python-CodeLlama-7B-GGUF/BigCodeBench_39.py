
import numpy as np
from scipy.stats import ttest_1samp
import matplotlib.pyplot as plt

# Constants
ALPHA = 0.05

def task_func(data_matrix):
    # Calculate the mean of each row in the data matrix
    means = np.mean(data_matrix, axis=1)

    # Run a t-test on each mean against the population mean
    t_stats, p_values = ttest_1samp(means, np.mean(data_matrix))

    # Identify the indices of the means that are significantly different from the population mean
    significant_indices = np.where(p_values < ALPHA)[0]

    # Create a line plot with the mean of rows in red
    ax = plt.plot(means, color='red', label='Means')

    # Create a line plot with the significant means on the x-axis and the corresponding means on the y-axis
    ax = plt.plot(significant_indices, means[significant_indices], 'bo', label='Significant Means')

    # Create an horizontal line which represents the mean computed on the whole 2D matrix
    ax = plt.axhline(np.mean(data_matrix), color='green', label='Population Mean')

    # Set the labels and title of the plot
    ax.set_xlabel('Indices')
    ax.set_ylabel('Means')
    ax.set_title('Means and Significant Means')

    # Return the list of significant indices and the plot
    return significant_indices, ax