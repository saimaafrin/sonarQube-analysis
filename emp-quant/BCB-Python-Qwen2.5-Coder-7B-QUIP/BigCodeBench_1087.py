
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def task_func(mean=123456.908, std_dev=1.2, save_plots=False):
    # Generate a random sample from a normal distribution
    sample = np.random.normal(loc=mean, scale=std_dev, size=1000)

    # Calculate skewness and kurtosis
    skewness = stats.skew(sample)
    kurtosis = stats.kurtosis(sample)

    # Create a histogram
    plt.figure()
    plt.hist(sample, bins=30, density=True)
    plt.title('Histogram of the Sample')
    plt.xlabel('Value')
    plt.ylabel('Density')
    if save_plots:
        plt.savefig('histogram.png')
    plt.close()

    # Create a QQ plot
    plt.figure()
    stats.probplot(sample, dist='norm', plot=plt)
    plt.title('QQ Plot of the Sample')
    if save_plots:
        plt.savefig('qq_plot.png')
    plt.close()

    # Return the results
    return skewness, kurtosis, ['histogram.png', 'qq_plot.png'] if save_plots else []