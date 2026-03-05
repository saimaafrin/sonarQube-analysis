import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
def task_func(mean=123456.908, std_dev=1.2, save_plots=False):
    """
    Generate a random sample from a normal distribution, analyze its skewness and kurtosis, and create a histogram and a QQ plot to visualize the distribution.
    """
    # Generate a random sample from a normal distribution
    sample = np.random.normal(mean, std_dev, 1000)

    # Analyze the sample's skewness and kurtosis
    skewness = stats.skew(sample)
    kurtosis = stats.kurtosis(sample)

    # Create a histogram and a QQ plot to visualize the distribution
    fig, axs = plt.subplots(2, 1, figsize=(10, 10))
    axs[0].hist(sample, bins=50, density=True, alpha=0.5, label='Histogram')
    axs[1].plot(sample, label='QQ Plot')
    axs[1].legend()

    # Save the plots if requested
    if save_plots:
        fig.savefig('histogram.png')
        fig.savefig('qq_plot.png')

    # Return the skewness and kurtosis of the sample
    return skewness, kurtosis, ['histogram.png', 'qq_plot.png']
mean = 123456.908
std_dev = 1.2
save_plots = False