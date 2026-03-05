
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def task_func(mean=123456.908, std_dev=1.2, save_plots=False):
    # Generate a random sample from a normal distribution
    sample = stats.norm.rvs(mean, std_dev, size=1000)

    # Calculate the skewness and kurtosis of the sample
    skewness = stats.skewness(sample)
    kurtosis = stats.kurtosis(sample)

    # Plot the histogram and QQ plot
    if save_plots:
        plt.hist(sample, bins=50, normed=True, facecolor='green', alpha=0.5)
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.savefig('histogram.png')
        plt.clf()
        plt.xlabel('Theoretical quantiles')
        plt.ylabel('Theoretical quantiles')
        plt.savefig('qqplot.png')
    else:
        plt.hist(sample, bins=50, normed=True, facecolor='green', alpha=0.5)
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.show()
        plt.xlabel('Theoretical quantiles')
        plt.ylabel('Theoretical quantiles')
        plt.show()

    return skewness, kurtosis, ['histogram.png', 'qqplot.png']