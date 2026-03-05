import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from itertools import chain
def task_func(L):
    # Flatten the list of lists into a single list
    flattened_list = list(chain.from_iterable(L))
    
    # Convert the flattened list into a numpy array
    data = np.array(flattened_list)
    
    # Fit a normal distribution to the data
    mu, std = norm.fit(data)
    
    # Create a histogram of the data
    plt.hist(data, bins=30, density=True, alpha=0.6, color='g')
    
    # Plot the fitted normal distribution
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    plt.plot(x, p, 'k', linewidth=2)
    
    # Return the Axes object
    return plt.gca()