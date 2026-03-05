import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
def task_func(size=1000):
    """
    Generate a list of normally distributed random numbers and plot their histogram and probability density function (PDF).
    """
    # Generate normally distributed random numbers
    data = stats.norm.rvs(size=size, loc=0, scale=1)

    # Plot histogram
    fig, ax = plt.subplots()
    ax.hist(data, bins=50, density=True, alpha=0.5, label='Histogram')
    ax.set_xlabel('Value')
    ax.set_ylabel('Density')
    ax.set_title('Histogram of Normally Distributed Random Numbers')
    ax.legend()

    # Plot PDF
    ax2 = ax.twinx()
    ax2.plot(stats.norm.pdf(data), label='PDF')
    ax2.set_ylabel('Probability Density')
    ax2.set_title('Probability Density Function of Normally Distributed Random Numbers')
    ax2.legend()

    return fig