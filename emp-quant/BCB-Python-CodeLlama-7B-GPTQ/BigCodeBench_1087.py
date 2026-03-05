import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
def task_func(mean=123456.908, std_dev=1.2, save_plots=False):
    # Generate a random sample from a normal distribution
    sample = np.random.normal(mean, std_dev, size=1000)

    # Analyze the skewness and kurtosis of the sample
    skewness = stats.skew(sample)
    kurtosis = stats.kurtosis(sample)

    # Create a histogram and a QQ plot to visualize the distribution
    fig, axs = plt.subplots(2, 1, figsize=(10, 6))
    axs[0].hist(sample, bins=50)
    axs[1].plot(stats.norm.ppf(stats.norm.cdf(sample)), label='QQ plot')
    axs[1].legend()

    # Save the plots if requested
    if save_plots:
        fig.savefig('histogram.png')
        axs[1].get_figure().savefig('qq_plot.png')

    # Return the results
    return skewness, kurtosis, ['histogram.png', 'qq_plot.png']