
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

def task_func(mean, std_dev, num_samples):
    # Generate samples from the normal distribution
    samples = np.random.normal(mean, std_dev, num_samples)

    # Create a histogram of the samples
    hist, bins = np.histogram(samples, bins=30)

    # Normalize the histogram
    hist = hist / len(samples)

    # Create a plot of the histogram and the PDF
    fig, ax = plt.subplots()
    ax.bar(bins[:-1], hist, width=bins[1] - bins[0])
    ax.plot(bins, norm.pdf(bins, mean, std_dev), 'r-')

    # Set the plot title
    ax.set_title(f'Fit results: mean = {mean:.2f}, std = {std_dev:.2f}')

    # Return the figure and the samples
    return fig, samples