import numpy as np
from scipy.stats import ttest_1samp
import matplotlib.pyplot as plt
ALPHA = 0.05
def task_func(data_matrix):
    """
    Calculate the mean value of each row in a 2D data matrix, run a t-test from a sample against the population value,
    and record the mean values that differ significantly.
    
    Parameters:
    data_matrix (np.array): A 2D numpy array of numerical data.
    
    Returns:
    tuple: A tuple containing:
        list: A list of indices of the means that are significantly different from the population mean.
        Axes: The plot showing the means and significant means.
    """
    # Calculate the mean of each row
    row_means = np.mean(data_matrix, axis=1)
    
    # Calculate the population mean
    population_mean = np.mean(data_matrix)
    
    # Perform t-test for each row mean against the population mean
    t_stat, p_values = ttest_1samp(data_matrix, population_mean, axis=1)
    
    # Find indices of rows with p-value less than ALPHA
    significant_indices = np.where(p_values < ALPHA)[0]
    
    # Create a figure and axis for plotting
    fig, ax = plt.subplots()
    
    # Plot the means of rows in red
    ax.plot(range(len(row_means)), row_means, 'ro-', label='Means')
    
    # Plot the significant means in blue
    ax.plot(significant_indices, row_means[significant_indices], 'bo-', label='Significant Means')
    
    # Plot the population mean as a horizontal line in green
    ax.axhline(y=population_mean, color='g', linestyle='--', label='Population Mean')
    
    # Set labels and title
    ax.set_xlabel('Row Index')
    ax.set_ylabel('Mean Value')
    ax.set_title('Row Means and Significant Means')
    
    # Add legend
    ax.legend()
    
    # Show the plot
    plt.show()
    
    # Return the significant indices and the plot
    return significant_indices, ax