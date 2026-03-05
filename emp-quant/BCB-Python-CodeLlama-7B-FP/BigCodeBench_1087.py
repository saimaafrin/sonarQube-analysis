import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
def task_func(mean=123456.908, std_dev=1.2, save_plots=False):
    """
    Generate a random sample from a normal distribution, analyze its skewness and kurtosis, and create a histogram and a QQ plot to visualize the distribution.
    The function should output with:
        float: Skewness of the sample.
        float: Kurtosis of the sample.
        list: Paths to the saved plot files, empty if save_plots is False.
    """
    # Generate a random sample from a normal distribution
    sample = np.random.normal(mean, std_dev, size=1000)

    # Analyze the skewness and kurtosis of the sample
    skewness = stats.skew(sample)
    kurtosis = stats.kurtosis(sample)

    # Create a histogram and a QQ plot to visualize the distribution
    fig, axs = plt.subplots(2, 1, figsize=(10, 6))
    axs[0].hist(sample, bins=50, density=True)
    axs[1].plot(stats.norm.ppf(stats.norm.cdf(sample), loc=mean, scale=std_dev), 'r-')
    axs[1].set_xlabel('Value')
    axs[1].set_ylabel('Density')
    axs[1].set_title('Q-Q Plot')
    if save_plots:
        fig.savefig('histogram.png')
        fig.savefig('qq_plot.png')
    return skewness, kurtosis, ['histogram.png', 'qq_plot.png']