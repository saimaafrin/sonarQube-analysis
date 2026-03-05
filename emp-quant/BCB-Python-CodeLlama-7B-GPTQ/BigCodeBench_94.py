import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
def task_func(mean, std_dev, num_samples):
    # Generate samples from a normal distribution
    samples = np.random.normal(mean, std_dev, num_samples)

    # Create a histogram of the samples
    hist, bins = np.histogram(samples, bins=30)

    # Create a figure and axis object
    fig, ax = plt.subplots()

    # Plot the histogram
    ax.bar(bins[:-1], hist, width=bins[1] - bins[0])

    # Overlay the probability density function (PDF) of the normal distribution
    x = np.linspace(mean - 3 * std_dev, mean + 3 * std_dev, 100)
    ax.plot(x, norm.pdf(x, mean, std_dev), 'r--')

    # Set the title of the plot
    ax.set_title(f'Fit results: mean = {mean:.2f}, std = {std_dev:.2f}')

    # Return the figure and samples
    return fig, samples
mean = 0
std_dev = 1
num_samples = 1000