
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def task_func(mu, sigma, num_samples=1000, seed=77):
    # Generate a normal distribution with the given mean and standard deviation
    samples = stats.norm.rvs(mu, sigma, size=num_samples, random_state=seed)

    # Create a histogram of the samples
    hist_bins = np.linspace(0, 10, 100)
    hist, _ = np.histogram(samples, bins=hist_bins)

    # Create a Q-Q plot of the samples
    qq_bins = np.linspace(0, 10, 100)
    qq_values = stats.norm.ppf(qq_bins, mu, sigma)

    # Create a figure with the histogram and Q-Q plot
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.hist(samples, bins=hist_bins, alpha=0.5, label='Histogram')
    ax.plot(qq_values, qq_bins, 'b-', label='Q-Q plot')
    ax.set_xlabel('Value')
    ax.set_ylabel('Count')
    ax.legend()
    return fig