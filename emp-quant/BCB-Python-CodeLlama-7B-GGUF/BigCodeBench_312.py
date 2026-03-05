
import random
import matplotlib.pyplot as plt

# Constants
DISTRIBUTION_SIZE = 1000

def task_func(bins=30):
    # Generate a Gaussian distribution
    distribution = [random.gauss(0, 1) for _ in range(DISTRIBUTION_SIZE)]

    # Plot the histogram
    fig, ax = plt.subplots()
    ax.hist(distribution, bins=bins, density=True, alpha=0.5, label='Gaussian distribution')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title('Gaussian Distribution')
    ax.legend()

    return distribution, ax

# Call the function
distribution, ax = task_func()

# Show the plot
plt.show()