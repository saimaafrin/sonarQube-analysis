
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

def task_func(length):
    # Create a normal distribution with mean 0 and standard deviation 1
    dist = norm.rvs(0, 1, size=length)

    # Plot the histogram of the distribution
    fig, ax = plt.subplots()
    ax.hist(dist, bins=50)
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    ax.set_title("Histogram of Normal Distribution")

    # Plot the probability density function
    ax2 = ax.twinx()
    x = np.linspace(0, 1, 100)
    ax2.plot(x, norm.pdf(x), '--k')
    ax2.set_ylabel("Probability Density")
    ax2.set_xlabel("Value")
    ax2.set_title("Probacy Density Function")

    return dist, fig