import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
def task_func(mean=123456.908, std_dev=1.2, save_plots=False):
    """
    Generate a random sample from a normal distribution, analyze its skewness and kurtosis,
    and create a histogram and a QQ plot to visualize the distribution.

    Parameters:
    - mean (float, optional): Mean of the normal distribution. Defaults to 123456.908.
    - std_dev (float, optional): Standard deviation of the normal distribution. Defaults to 1.2.
    - save_plots (bool, optional): If True, saves the plots to files. Defaults to False.

    Returns:
    - float: Skewness of the sample.
    - float: Kurtosis of the sample.
    - list: Paths to the saved plot files, empty if save_plots is False.

    Requirements:
    - numpy
    - matplotlib.pyplot
    - scipy.stats

    Example:
    >>> np.random.seed(0)
    >>> skewness, kurtosis, plot_paths = task_func(123456.908, 1.2, True)
    >>> print(f'Skewness: {skewness}, Kurtosis: {kurtosis}, Plots: {plot_paths}')
    Skewness: 0.03385895323538189, Kurtosis: -0.04676632447765128, Plots: ['histogram_plot.png', 'qq_plot.png']

    """

    # Generate a random sample from a normal distribution
    sample = np.random.normal(mean, std_dev, 10000)

    # Analyze the sample's skewness and kurtosis
    skewness = stats.skew(sample)
    kurtosis = stats.kurtosis(sample)

    # Create a histogram and a QQ plot to visualize the distribution
    histogram_plot_path = None
    qq_plot_path = None
    if save_plots:
        histogram_plot_path = 'histogram_plot.png'
        qq_plot_path = 'qq_plot.png'
        plt.hist(sample, bins=100)
        plt.savefig(histogram_plot_path)
        plt.clf()
        plt.plot(sample, stats.norm.ppf(stats.norm.cdf(sample)), 'o')
        plt.savefig(qq_plot_path)

    return skewness, kurtosis, [histogram_plot_path, qq_plot_path]