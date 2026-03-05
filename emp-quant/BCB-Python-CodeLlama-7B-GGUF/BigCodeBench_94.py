
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
    ax.bar(bins[:-1], hist, width=bins[1]-bins[0], align='edge')

    # Overlay the probability density function
    x = np.linspace(bins[0], bins[-1], 1000)
    y = norm.pdf(x, mean, std_dev)
    ax.plot(x, y, color='red', linewidth=2)

    # Set the title of the plot
    title = f"Fit results: mean = {mean:.2f}, std = {std_dev:.2f}"
    ax.set_title(title)

    # Return the figure and samples
    return fig, samples