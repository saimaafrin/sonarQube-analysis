import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
def task_func(arr: np.ndarray) -> (plt.Axes, np.ndarray):
    """
    Plots a histogram of normalized data from an input 2D numpy array alongside the probability density function (PDF) of a standard normal distribution.

    Args:
        arr (np.ndarray): Input 2D numpy array.

    Returns:
        A tuple containing:
            A matplotlib Axes object with the histogram of the normalized data and the overlaid standard normal PDF.
            The normalized data as a 1D numpy array.
    """
    # Calculate the sum of elements in each row of the array
    row_sums = arr.sum(axis=1)

    # Normalize the row sums to have a mean of 0 and a standard deviation of 1
    mean = row_sums.mean()
    std = row_sums.std()
    if std == 0:
        normalized_row_sums = np.zeros_like(row_sums)
    else:
        normalized_row_sums = (row_sums - mean) / std

    # Plot the histogram of the normalized data
    fig, ax = plt.subplots()
    ax.hist(normalized_row_sums, bins=30, density=True, alpha=0.6, color='green')
    ax.set_title('Histogram of Normalized Data with Standard Normal PDF')

    # Overlay the PDF of a standard normal distribution on the histogram for comparison
    x = np.linspace(-3, 3, 1000)
    y = norm.pdf(x)
    ax.plot(x, y, color='red', linewidth=2)

    # Return the matplotlib Axes object and the normalized data
    return ax, normalized_row_sums
arr = np.random.rand(10, 10)