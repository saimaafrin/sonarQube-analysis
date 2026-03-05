
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def task_func(arr: np.ndarray) -> (plt.Axes, np.ndarray):
    # Calculate row sums
    row_sums = np.sum(arr, axis=1)
    
    # Normalize the row sums
    mean = np.mean(row_sums)
    std = np.std(row_sums)
    normalized_data = (row_sums - mean) / std
    
    # Plot the histogram
    fig, ax = plt.subplots()
    ax.hist(normalized_data, bins=30, density=True, alpha=0.6, color='green')
    
    # Plot the PDF of a standard normal distribution
    x = np.linspace(-3, 3, 100)
    pdf = norm.pdf(x, 0, 1)
    ax.plot(x, pdf, color='red', linewidth=2)
    
    # Set the title of the plot
    ax.set_title('Histogram of Normalized Data with Standard Normal PDF')
    
    # Set the range of the PDF curve to cover 99% of a standard normal distribution
    ax.set_xlim(-3, 3)
    
    # Return the Axes object and the normalized data
    return ax, normalized_data