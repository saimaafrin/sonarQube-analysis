
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def task_func(size=1000):
    # Generate a list of normally distributed random numbers
    random_numbers = stats.norm.rvs(size=size, loc=0, scale=1)

    # Plot the histogram
    fig, ax = plt.subplots()
    ax.hist(random_numbers, bins=50)
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    ax.set_title("Histogram of Normally Distributed Random Numbers")

    # Plot the probability density function
    ax2 = ax.twinx()
    x = np.linspace(0, 1, 1000)
    ax2.plot(x, stats.norm.pdf(x), c="red")
    ax2.set_ylabel("Probability Density")
    ax2.set_xlabel("Value")
    ax2.set_title("Probability Density Function of Normally Distributed Random Numbers")

    return fig

# Generate and plot the histogram and probability density function
fig = task_func(size=1000)