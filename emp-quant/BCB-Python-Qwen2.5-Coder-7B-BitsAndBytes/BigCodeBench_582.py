
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def task_func(size=1000):
    # Generate normally distributed random numbers
    data = np.random.normal(loc=0, scale=1, size=size)
    
    # Create a figure object
    fig, ax = plt.subplots()
    
    # Plot the histogram
    n, bins, patches = ax.hist(data, bins=30, density=True, alpha=0.6, color='g')
    
    # Calculate the PDF values for plotting
    xmin, xmax = ax.get_xlim()
    x = np.linspace(xmin, xmax, 100)
    p = stats.norm.pdf(x, loc=0, scale=1)
    
    # Plot the PDF
    ax.plot(x, p, 'k', linewidth=2)
    
    # Set labels and title
    ax.set_xlabel('Value')
    ax.set_ylabel('Probability Density')
    ax.set_title('Histogram and PDF of Normally Distributed Random Numbers')
    
    return fig