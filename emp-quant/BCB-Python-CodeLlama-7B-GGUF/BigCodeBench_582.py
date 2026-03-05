
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def task_func(size=1000):
    # Generate normally distributed random numbers
    x = np.random.normal(size=size)

    # Plot histogram
    plt.hist(x, bins=50, alpha=0.5, label='Histogram')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram of Normally Distributed Random Numbers')
    plt.legend()

    # Plot probability density function
    plt.plot(x, stats.norm.pdf(x), label='Probability Density Function')
    plt.xlabel('Value')
    plt.ylabel('Probability')
    plt.title('Probability Density Function of Normally Distributed Random Numbers')
    plt.legend()

    # Show the plot
    plt.show()

# Call the function
task_func()