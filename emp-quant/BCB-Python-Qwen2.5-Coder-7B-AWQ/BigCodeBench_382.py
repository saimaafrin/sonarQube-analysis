import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
def task_func(length):
    """
    Generates a normal distribution with a given length, plots its histogram alongside the probability density function,
    and returns the distribution and the plot.

    Parameters:
    length (int): The number of samples in the normal distribution.

    Returns:
    tuple: A tuple containing:
        1. numpy array with the normal distribution.
        2. matplotlib Axes object representing the plot.
    """
    # Generate the normal distribution
    data = norm.rvs(loc=0, scale=1, size=length)
    
    # Create a figure and axis for plotting
    fig, ax = plt.subplots()
    
    # Plot the histogram of the data
    ax.hist(data, bins=30, density=True, alpha=0.6, color='g')
    
    # Plot the probability density function
    x = np.linspace(-3, 3, 100)
    ax.plot(x, norm.pdf(x, loc=0, scale=1), 'r-', lw=2)
    
    # Set the title and labels
    ax.set_title('Normal Distribution')
    ax.set_xlabel('Value')
    ax.set_ylabel('Probability Density')
    
    # Return the data and the plot
    return data, ax