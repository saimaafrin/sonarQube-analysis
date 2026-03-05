
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def task_func(size=1000):
    # Generate normally distributed random numbers
    data = np.random.normal(0, 1, size)
    
    # Create a figure object
    fig, ax = plt.subplots()
    
    # Plot the histogram
    ax.hist(data, bins=30, density=True, alpha=0.6, color='g')
    
    # Plot the PDF
    x = np.linspace(-3, 3, 100)
    ax.plot(x, stats.norm.pdf(x, 0, 1), 'r-', lw=2)
    
    # Set the title and labels
    ax.set_title('Histogram and PDF of Normally Distributed Data')
    ax.set_xlabel('Value')
    ax.set_ylabel('Density')
    
    # Return the figure object
    return fig