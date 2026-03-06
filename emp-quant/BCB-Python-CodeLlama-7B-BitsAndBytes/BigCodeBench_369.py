
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def task_func(l):
    # Calculate the mean and standard deviation of the array
    mean = np.mean(l)
    std = np.std(l)

    # Create a histogram of the array
    n, bins, patches = plt.hist(l, 50, density=True, facecolor='g', alpha=0.75)

    # Add a Gaussian fit to the histogram
    x = np.linspace(min(l), max(l), 100)
    y = stats.norm.pdf(x, mean, std)
    plt.plot(x, y, 'r-', linewidth=2)

    # Set the title of the plot
    plt.title(f'Fit results: mu = {mean:.2f}, std = {std:.2f}')

    # Show the plot
    plt.show()