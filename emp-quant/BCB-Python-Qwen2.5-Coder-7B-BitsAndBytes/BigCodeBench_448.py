
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def task_func(mu=0, sigma=1):
    """
    Draws and returns a subplot of a normal distribution with the given mean (mu) and standard deviation (sigma).
    
    Parameters:
    mu (float): The mean of the normal distribution.
    sigma (float): The standard deviation of the normal distribution.
    
    Returns:
    matplotlib.axes.Axes: The subplot representing the normal distribution.
    """
    # Create an array of 100 linearly spaced numbers between mu - 3*sigma and mu + 3*sigma
    x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)
    
    # Calculate the y values for the normal distribution using the norm.pdf function
    y = norm.pdf(x, mu, sigma)
    
    # Create a figure and a set of subplots
    fig, ax = plt.subplots()
    
    # Plot the normal distribution
    ax.plot(x, y, label=f'Normal Distribution ($\mu={mu}, \sigma={sigma}$)')
    
    # Add labels and title
    ax.set_xlabel('x')
    ax.set_ylabel('Probability Density')
    ax.set_title('Normal Distribution Subplot')
    ax.legend()
    
    # Return the axes object
    return ax