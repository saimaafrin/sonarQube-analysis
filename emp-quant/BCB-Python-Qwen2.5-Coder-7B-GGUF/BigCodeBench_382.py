
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

def task_func(length):
    # Generate a normal distribution with mean 0 and standard deviation 1
    distribution = np.random.normal(0, 1, length)
    
    # Create a figure and axis for plotting
    fig, ax = plt.subplots()
    
    # Plot the histogram of the distribution
    ax.hist(distribution, bins=30, density=True, alpha=0.6, color='g')
    
    # Plot the probability density function
    x = np.linspace(-3, 3, 100)
    ax.plot(x, norm.pdf(x, 0, 1), 'r-', lw=2)
    
    # Set the title and labels
    ax.set_title('Normal Distribution')
    ax.set_xlabel('Value')
    ax.set_ylabel('Probability Density')
    
    # Return the distribution and the plot
    return distribution, ax