import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
def task_func(mean, std_dev, num_samples):
    """
    Generates a histogram of samples drawn from a normal distribution and overlays the probability density function (PDF) of the normal distribution.
    The plot is titled with the fit results, showing the mean and standard deviation used in the generation.
    The function returns both the plot and the samples generated.
    """
    # Generate samples from the normal distribution
    samples = norm.rvs(mean, std_dev, size=num_samples)

    # Create a histogram of the samples
    hist, bins = np.histogram(samples, bins=30)

    # Normalize the histogram
    hist = hist / hist.sum()

    # Create a figure and axis object
    fig, ax = plt.subplots()

    # Plot the histogram
    ax.bar(bins[:-1], hist, width=bins[1] - bins[0], align='edge', alpha=0.5)

    # Overlay the PDF of the normal distribution
    x = np.linspace(bins[0], bins[-1], 1000)
    y = norm.pdf(x, mean, std_dev)
    ax.plot(x, y, label='PDF', color='red', linewidth=2)

    # Set the title of the plot
    title = f'Fit results: mean = {mean:.2f}, std = {std_dev:.2f}'
    ax.set_title(title)

    # Set the x-axis label
    ax.set_xlabel('Value')

    # Set the y-axis label
    ax.set_ylabel('Frequency')

    # Set the legend
    ax.legend()

    # Return the figure and samples
    return fig, samples
mean = 0
std_dev = 1
num_samples = 1000