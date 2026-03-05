import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
def task_func(arr: np.ndarray) -> (plt.Axes, np.ndarray):
    # Calculate the sum of elements in each row
    row_sums = np.sum(arr, axis=1)
    
    # Calculate mean and standard deviation of the row sums
    mean = np.mean(row_sums)
    std_dev = np.std(row_sums)
    
    # Normalize the row sums
    if std_dev == 0:
        normalized_data = np.zeros_like(row_sums)
    else:
        normalized_data = (row_sums - mean) / std_dev
    
    # Plotting the histogram
    fig, ax = plt.subplots()
    ax.hist(normalized_data, bins=30, density=True, alpha=0.6, color='green')
    
    # Plotting the standard normal PDF
    x = np.linspace(-3, 3, 100)  # Range to cover 99% of a standard normal distribution
    pdf = norm.pdf(x, 0, 1)
    ax.plot(x, pdf, 'r-', linewidth=2)
    
    # Setting the title of the plot
    ax.set_title('Histogram of Normalized Data with Standard Normal PDF')
    
    return ax, normalized_data