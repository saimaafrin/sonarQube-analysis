import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
def task_func(mu, sigma, num_samples=1000, seed=77):
    """
    Generate a normal distribution with the given mean and standard deviation.
    Creates a figure containing a histogram and a Q-Q plot of the generated samples.

    Args:
        mu (float): The mean of the normal distribution.
        sigma (float): The standard deviation of the normal distribution.
        num_samples (int, optional): The number of samples to generate. Defaults to 1000.
        seed (int, optional): The random seed to use. Defaults to 77.

    Returns:
        matplotlib.figure.Figure: A matplotlib figure containing the histogram and Q-Q plot.
    """
    np.random.seed(seed)
    samples = np.random.normal(mu, sigma, num_samples)

    # Create a histogram of the samples
    hist, bins = np.histogram(samples, bins=50, density=True)
    hist = hist / np.sum(hist)
    plt.bar(bins[:-1], hist, width=bins[1] - bins[0], align='edge')
    plt.xlabel('Value')
    plt.ylabel('Probability')
    plt.title('Histogram of Generated Samples')

    # Create a Q-Q plot of the samples
    qq_data = stats.norm.ppf(np.linspace(0.01, 0.99, 100))
    plt.plot(qq_data, qq_data, 'k--', label='Theoretical Quantiles')
    plt.plot(samples, 'bo', label='Generated Samples')
    plt.xlabel('Theoretical Quantiles')
    plt.ylabel('Generated Samples')
    plt.title('Q-Q Plot of Generated Samples')
    plt.legend()

    return plt.gcf()
mu = 0
sigma = 1
num_samples = 1000
seed = 77