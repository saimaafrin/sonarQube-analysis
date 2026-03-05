import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
def task_func(size=1000):
    # Generate normally distributed random numbers
    data = np.random.normal(loc=0, scale=1, size=size)
    
    # Create a figure object
    fig, ax = plt.subplots()
    
    # Plot histogram
    ax.hist(data, bins=30, density=True, alpha=0.6, color='g')
    
    # Plot probability density function
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = stats.norm.pdf(x, 0, 1)
    ax.plot(x, p, 'k', linewidth=2)
    
    # Set labels and title
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram and PDF of Normally Distributed Random Numbers')
    
    return fig