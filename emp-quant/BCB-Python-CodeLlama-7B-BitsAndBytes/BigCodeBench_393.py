
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def task_func(mu, sigma, num_samples=1000, seed=77):
    # Generate a normal distribution with the given mean and standard deviation
    np.random.seed(seed)
    samples = np.random.normal(mu, sigma, num_samples)

    # Create a histogram of the samples
    hist, bins = np.histogram(samples, bins=50, density=True)
    hist_plot = plt.bar(bins[:-1], hist, width=bins[1] - bins[0], align='edge')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram of Normal Distribution')

    # Create a Q-Q plot of the samples
    qq_plot = plt.plot(stats.norm.ppf(stats.ecdf(samples)), bins[:-1], 'o-')
    plt.xlabel('Theoretical quantiles')
    plt.ylabel('Empirical quantiles')
    plt.title('Q-Q Plot of Normal Distribution')

    # Create a figure containing both plots
    fig = plt.figure(figsize=(8, 6))
    fig.add_subplot(111)
    plt.subplot(111)
    plt.plot(hist_plot)
    plt.plot(qq_plot)
    plt.legend(['Histogram', 'Q-Q Plot'])
    plt.show()

    return fig