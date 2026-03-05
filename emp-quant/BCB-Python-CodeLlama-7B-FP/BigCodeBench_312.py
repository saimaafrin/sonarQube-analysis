import random
import matplotlib.pyplot as plt
DISTRIBUTION_SIZE = 1000
def task_func(bins=30):
    """
    Generate a Gaussian distribution and plot its histogram.

    Args:
        bins (int): Number of bins for the histogram.

    Returns:
        tuple: A tuple containing the distribution list and the Axes patch object of the histogram plot.
    """
    # Generate a Gaussian distribution
    distribution = [random.gauss(0, 1) for _ in range(DISTRIBUTION_SIZE)]

    # Plot the histogram
    fig, ax = plt.subplots()
    ax.hist(distribution, bins=bins, density=True, alpha=0.5, label='Gaussian distribution')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title('Gaussian Distribution Histogram')
    ax.legend()

    return distribution, ax