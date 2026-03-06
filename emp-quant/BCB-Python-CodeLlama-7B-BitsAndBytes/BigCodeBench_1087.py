
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
    hist, bins = np.histogram(sample, bins=20, density=True)
    plt.hist(bins, hist, density=True, alpha=0.5, label='Histogram')
    plt.plot(bins, stats.norm.pdf(bins, mean, std_dev), label='Normal distribution')
    plt.legend()
    plt.title('Skewness: {:.2f}, Kurtosis: {:.2f}'.format(skewness, kurtosis))
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()

    # Save the plots if requested
    if save_plots:
        hist_path = 'histogram.png'
        qq_path = 'qq_plot.png'
        plt.savefig(hist_path)
        plt.savefig(qq_path)
        return [hist_path, qq_path]
    else:
        return []