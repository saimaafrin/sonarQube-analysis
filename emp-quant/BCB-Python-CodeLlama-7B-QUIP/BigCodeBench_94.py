
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

def task_func(mean, std_dev, num_samples):
    # Generate samples from the normal distribution
    samples = np.random.normal(mean, std_dev, size=num_samples)

    # Plot the histogram of the samples
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    ax.hist(samples, bins=30)
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    ax.set_title("Fit results: mean = %.2f, std = %.2f" % (mean, std_dev))
    plt.show()

    # Return the figure and the samples
    return fig, samples