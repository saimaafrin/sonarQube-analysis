
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def task_func(arr: np.ndarray) -> (plt.Axes, np.ndarray):
    # Calculate the sum of elements in each row
    row_sums = np.sum(arr, axis=1)
    
    # Check if there is any zero standard deviation
    std_dev = np.std(row_sums)
    if std_dev == 0:
        normalized_data = np.zeros_like(row_sums)
    else:
        # Normalize the row sums
        normalized_data = (row_sums - np.mean(row_sums)) / std_dev
    
    # Plotting the histogram
    fig, ax = plt.subplots()
    n, bins, patches = ax.hist(normalized_data, bins=30, density=True, alpha=0.6, color='green')
    
    # Overlay the PDF of a standard normal distribution
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, 0, 1)
    ax.plot(x, p, 'r-', linewidth=2)
    
    # Set the title of the plot
    ax.set_title('Histogram of Normalized Data with Standard Normal PDF')
    
    return ax, normalized_data