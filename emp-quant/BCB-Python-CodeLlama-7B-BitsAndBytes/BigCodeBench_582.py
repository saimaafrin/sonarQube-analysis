
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def task_func(size=1000):
    # Generate normally distributed random numbers
    x = np.random.normal(size=size)

    # Plot histogram
    plt.hist(x, bins=50, density=True, alpha=0.5, label='Histogram')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram of Normally Distributed Random Numbers')
    plt.legend()

    # Plot probability density function
    x_range = np.linspace(x.min(), x.max(), 1000)
    pdf = stats.norm.pdf(x_range, loc=x.mean(), scale=x.std())
    plt.plot(x_range, pdf, label='Probability Density Function')
    plt.xlabel('Value')
    plt.ylabel('Probability Density')
    plt.title('Probability Density Function of Normally Distributed Random Numbers')
    plt.legend()

    # Show the plot
    plt.show()

# Call the function
task_func()