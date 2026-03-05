
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from itertools import chain

def task_func(L):
    # Flatten the list of lists
    flattened = list(chain.from_iterable(L))
    
    # Fit a normal distribution to the data
    data = np.array(flattened)
    mu, sigma = norm.fit(data)
    
    # Create a histogram of the data
    fig, ax = plt.subplots()
    ax.hist(data, bins=30, density=True, alpha=0.6, color='g')
    
    # Plot the normal distribution fit
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, sigma)
    ax.plot(x, p, "b--", linewidth=2)
    
    return ax