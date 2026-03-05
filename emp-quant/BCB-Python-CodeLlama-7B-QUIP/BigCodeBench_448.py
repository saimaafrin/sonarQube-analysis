
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def task_func(mu=0, sigma=1):
    # Create an array of 100 linearly spaced numbers between mu - 3*sigma and mu + 3*sigma
    x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)

    # Create a normal distribution object
    dist = norm(mu, sigma)

    # Draw the subplot representing the normal distribution
    ax = plt.axes()
    ax.plot(x, dist.pdf(x))

    return ax