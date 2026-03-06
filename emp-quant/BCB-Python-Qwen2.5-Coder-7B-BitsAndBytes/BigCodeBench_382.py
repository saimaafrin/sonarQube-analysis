
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

def task_func(length):
    # Constants for mean and standard deviation
    MU = 0
    SIGMA = 1
    
    # Generate the normal distribution
    data = np.random.normal(MU, SIGMA, length)
    
    # Create a figure and axis for plotting
    fig, ax = plt.subplots()
    
    # Plot the histogram of the generated data
    ax.hist(data, bins=30, density=True, alpha=0.6, color='g')
    
    # Plot the probability density function
    x = np.linspace(-3, 3, 100)
    y = norm.pdf(x, MU, SIGMA)
    ax.plot(x, y, 'r-', lw=2)
    
    # Set labels and title
    ax.set_xlabel('Value')
    ax.set_ylabel('Probability Density')
    ax.set_title('Normal Distribution Histogram and PDF')
    
    # Return the data and the plot
    return data, ax

# Show the plot
plt.show()