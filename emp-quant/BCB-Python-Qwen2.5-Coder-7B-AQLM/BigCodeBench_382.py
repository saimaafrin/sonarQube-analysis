
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

def task_func(length):
    # Define the mean and standard deviation
    MU = 0
    SIGMA = 1
    
    # Generate the normal distribution
    distribution = np.random.normal(MU, SIGMA, length)
    
    # Create a histogram of the distribution
    fig, ax = plt.subplots()
    ax.hist(distribution, bins=30, density=True, alpha=0.6, color='g')
    
    # Plot the probability density function
    x = np.linspace(MU - 3*SIGMA, MU + 3*SIGMA, 100)
    ax.plot(x, norm.pdf(x, MU, SIGMA), 'r-', lw=2)
    
    # Set the title and labels
    ax.set_title('Normal Distribution')
    ax.set_xlabel('Value')
    ax.set_ylabel('Probability Density')
    
    # Return the distribution and the plot
    return distribution, ax