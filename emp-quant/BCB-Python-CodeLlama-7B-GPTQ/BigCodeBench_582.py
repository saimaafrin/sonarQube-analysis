import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
def task_func(size=1000):
    """
    Generate a list of normally distributed random numbers and plot their histogram and probability density function (PDF).

    Args:
        size (int): Number of random numbers to generate.

    Returns:
        matplotlib.figure.Figure: A figure object containing the histogram and PDF plot.
    """
    # Generate normally distributed random numbers
    random_numbers = np.random.normal(size=size)

    # Plot histogram
    fig, ax = plt.subplots()
    ax.hist(random_numbers, bins=50, alpha=0.5, label='Histogram')
    ax.set_xlabel('Random numbers')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram of normally distributed random numbers')

    # Plot PDF
    ax2 = ax.twinx()
    ax2.plot(stats.norm.pdf(random_numbers), label='PDF')
    ax2.set_ylabel('Probability density')
    ax2.set_title('Probability density function of normally distributed random numbers')

    # Add legend
    handles, labels = ax.get_legend_handles_labels()
    ax2.legend(handles, labels)

    return fig