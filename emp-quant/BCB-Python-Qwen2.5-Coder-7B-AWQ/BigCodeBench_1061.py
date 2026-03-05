import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
def task_func(arr: np.ndarray) -> (plt.Axes, np.ndarray):
    # Calculate the sum of elements in each row
    row_sums = np.sum(arr, axis=1)
    
    # Calculate the mean and standard deviation of the row sums
    mean = np.mean(row_sums)
    std = np.std(row_sums)
    
    # Normalize the row sums
    if std == 0:
        normalized_data = np.zeros_like(row_sums)
    else:
        normalized_data = (row_sums - mean) / std
    
    # Plot the histogram of the normalized data
    fig, ax = plt.subplots()
    ax.hist(normalized_data, bins=30, density=True, alpha=0.6, color='green')
    
    # Plot the PDF of a standard normal distribution
    x = np.linspace(norm.ppf(0.005), norm.ppf(0.995), 100)
    ax.plot(x, norm.pdf(x), 'r-', lw=2)
    
    # Set the title of the plot
    ax.set_title('Histogram of Normalized Data with Standard Normal PDF')
    
    return ax, normalized_data