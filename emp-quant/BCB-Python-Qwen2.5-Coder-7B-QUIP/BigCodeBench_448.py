
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def task_func(mu=0, sigma=1):
    # Create an array of 100 linearly spaced numbers between mu - 3*sigma and mu + 3*sigma
    x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
    
    # Calculate the corresponding y values using the normal distribution pdf
    y = norm.pdf(x, mu, sigma)
    
    # Create a subplot
    fig, ax = plt.subplots()
    
    # Plot the normal distribution
    ax.plot(x, y)
    
    # Return the subplot
    return ax