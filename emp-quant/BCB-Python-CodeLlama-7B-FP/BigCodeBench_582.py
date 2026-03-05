import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
def task_func(size=1000):
    """
    Generate a list of normally distributed random numbers and plot their histogram and probability density function (PDF).
    """
    # Generate normally distributed random numbers
    data = np.random.normal(size=size)

    # Plot histogram
    plt.hist(data, bins=50, alpha=0.5, label='Histogram')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram of Normally Distributed Random Numbers')
    plt.legend()

    # Plot PDF
    x = np.linspace(data.min(), data.max(), 1000)
    y = stats.norm.pdf(x, loc=data.mean(), scale=data.std())
    plt.plot(x, y, label='PDF')
    plt.xlabel('Value')
    plt.ylabel('Probability Density')
    plt.title('Probability Density Function of Normally Distributed Random Numbers')
    plt.legend()

    # Return figure object
    return plt.gcf()
size = 1000