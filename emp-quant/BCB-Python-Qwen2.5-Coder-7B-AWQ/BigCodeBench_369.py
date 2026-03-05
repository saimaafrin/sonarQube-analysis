import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
def task_func(l):
    # Convert the input list to a numpy array
    data = np.array(l)
    
    # Fit a Gaussian distribution to the data
    mu, std = stats.norm.fit(data)
    
    # Create a histogram of the data
    ax = plt.hist(data, bins=30, density=True, alpha=0.6, color='g')
    
    # Fit a Gaussian curve to the histogram
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = stats.norm.pdf(x, mu, std)
    plt.plot(x, p, 'k', linewidth=2)
    
    # Set the title of the plot with the fit results
    plt.title(f'Fit results: mu = {mu:.2f},  std = {std:.2f}')
    
    # Show the plot
    plt.show()
    
    # Return the Axes object
    return ax