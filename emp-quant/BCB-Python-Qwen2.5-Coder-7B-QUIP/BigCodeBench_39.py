
import numpy as np
from scipy.stats import ttest_1samp
import matplotlib.pyplot as plt
# Constants
ALPHA = 0.05

def task_func(data_matrix):
    # Calculate the mean of each row
    row_means = np.mean(data_matrix, axis=1)
    
    # Calculate the mean of the entire dataset
    population_mean = np.mean(data_matrix)
    
    # Perform t-tests for each row
    t_test_results = [ttest_1samp(row, population_mean) for row in data_matrix]
    
    # Get the indices of rows with significant differences
    significant_indices = [i for i, result in enumerate(t_test_results) if result.pvalue < ALPHA]
    
    # Create a line plot for the means
    fig, ax = plt.subplots()
    ax.plot(range(len(row_means)), row_means, 'r-', label='Means')
    
    # Create a line plot for the significant means
    ax.plot(significant_indices, [row_means[i] for i in significant_indices], 'b-', label='Significant Means')
    
    # Create a horizontal line for the population mean
    ax.axhline(y=population_mean, color='g', linestyle='--', label='Population Mean')
    
    # Set labels and title
    ax.set_xlabel('Row Index')
    ax.set_ylabel('Mean Value')
    ax.set_title('Row Means and Significant Means')
    ax.legend()
    
    # Show the plot
    plt.show()
    
    # Return the list of significant indices
    return significant_indices, ax