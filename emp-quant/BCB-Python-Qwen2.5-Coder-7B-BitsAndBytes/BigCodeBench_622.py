
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from itertools import chain

def task_func(L):
    # Flatten the list of lists into a single list
    flattened_list = list(chain.from_iterable(L))
    
    # Convert the flattened list to a NumPy array
    data = np.array(flattened_list)
    
    # Fit a normal distribution to the data
    mu, std = norm.fit(data)
    
    # Create a figure and axis for plotting
    fig, ax = plt.subplots()
    
    # Plot the histogram of the data
    n, bins, patches = ax.hist(data, bins=30, density=True, alpha=0.6, color='g')
    
    # Plot the fitted normal distribution
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    ax.plot(x, p, 'k', linewidth=2)
    
    # Add labels and title
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram with Fitted Normal Distribution')
    
    return ax