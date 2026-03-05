
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def task_func(mean=123456.908, std_dev=1.2, save_plots=False):
    # Generate a random sample from a normal distribution
    sample = np.random.normal(mean, std_dev, 1000)

    # Calculate the skewness and kurtosis of the sample
    skewness = stats.skew(sample)
    kurtosis = stats.kurtosis(sample)

    # Create a histogram and a QQ plot to visualize the distribution
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))
    ax1.hist(sample, bins=50, density=True, alpha=0.5)
    ax1.set_title('Histogram of the sample')
    ax2.plot(sample, sample, 'bo-', alpha=0.5)
    ax2.set_title('QQ plot of the sample')
    ax2.set_xlabel('Theoretical quantiles')
    ax2.set_ylabel('Sample quantiles')
    if save_plots:
        fig.savefig('histogram.png')
        fig.savefig('qq_plot.png')
    else:
        plt.show()

    return skewness, kurtosis, ['histogram.png', 'qq_plot.png']