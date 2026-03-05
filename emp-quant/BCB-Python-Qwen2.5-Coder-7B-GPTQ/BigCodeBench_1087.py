import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
def task_func(mean=123456.908, std_dev=1.2, save_plots=False):
    # Generate a random sample from a normal distribution
    sample = np.random.normal(mean, std_dev, 1000)
    
    # Calculate skewness and kurtosis
    skewness = stats.skew(sample)
    kurtosis = stats.kurtosis(sample)
    
    # Create a histogram
    plt.figure(figsize=(8, 4))
    plt.hist(sample, bins=30, density=True, alpha=0.6, color='g')
    plt.title('Histogram of the Sample')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    if save_plots:
        plt.savefig('histogram.png')
        plt.close()
    
    # Create a QQ plot
    plt.figure(figsize=(8, 4))
    stats.probplot(sample, dist="norm", plot=plt)
    plt.title('QQ Plot of the Sample')
    if save_plots:
        plt.savefig('qq_plot.png')
        plt.close()
    
    # Return the skewness, kurtosis, and paths to the saved plots
    plot_paths = ['histogram.png', 'qq_plot.png'] if save_plots else []
    return skewness, kurtosis, plot_paths