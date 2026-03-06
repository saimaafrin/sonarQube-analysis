
import numpy as np
from scipy.stats import ttest_1samp
import matplotlib.pyplot as plt

# Constants
ALPHA = 0.05

def task_func(data_matrix):
    # Calculate the mean of each row
    row_means = np.mean(data_matrix, axis=1)
    
    # Calculate the overall population mean
    population_mean = np.mean(row_means)
    
    # Perform t-tests for each row mean against the population mean
    t_stat, p_values = ttest_1samp(row_means, population_mean)
    
    # Identify indices where p-value < ALPHA
    significant_indices = np.where(p_values < ALPHA)[0]
    
    # Create a figure and axis for plotting
    fig, ax = plt.subplots()
    
    # Plot all row means in red
    ax.plot(range(len(row_means)), row_means, color='red', label='Means')
    
    # Plot significant means in blue
    ax.plot(significant_indices, row_means[significant_indices], color='blue', marker='o', linestyle='', label='Significant Means')
    
    # Plot the population mean as a horizontal line in green
    ax.axhline(population_mean, color='green', linestyle='--', label='Population Mean')
    
    # Set labels and legend
    ax.set_xlabel('Row Index')
    ax.set_ylabel('Mean Value')
    ax.legend()
    
    return significant_indices, ax