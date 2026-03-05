
import numpy as np
from scipy.stats import ttest_1samp
import matplotlib.pyplot as plt

# Constants
ALPHA = 0.05

def task_func(data_matrix):
    # Calculate the mean of each row
    row_means = np.mean(data_matrix, axis=1)
    
    # Calculate the population mean
    population_mean = np.mean(data_matrix)
    
    # Perform t-test for each row mean against the population mean
    t_stat, p_values = ttest_1samp(row_means, population_mean)
    
    # Find indices of rows with p-value less than ALPHA
    significant_indices = np.where(p_values < ALPHA)[0]
    
    # Create a line plot for the means
    fig, ax = plt.subplots()
    ax.plot(row_means, label='Means', color='red')
    
    # Create a line plot for the significant means
    ax.plot(significant_indices, row_means[significant_indices], label='Significant Means', color='blue')
    
    # Add a horizontal line for the population mean
    ax.axhline(population_mean, label='Population Mean', color='green')
    
    # Set labels and legend
    ax.set_xlabel('Row Index')
    ax.set_ylabel('Mean Value')
    ax.legend()
    
    # Return the indices of significant means and the plot
    return significant_indices.tolist(), ax