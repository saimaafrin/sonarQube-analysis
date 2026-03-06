
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def task_func(mean=123456.908, std_dev=1.2, save_plots=False):
    # Generate a random sample from a normal distribution
    sample_size = 1000
    sample = np.random.normal(loc=mean, scale=std_dev, size=sample_size)
    
    # Analyze skewness and kurtosis
    skewness = stats.skew(sample)
    kurtosis = stats.kurtosis(sample)
    
    # Create a histogram
    plt.figure(figsize=(10, 6))
    plt.hist(sample, bins=30, density=True, alpha=0.6, color='g')
    plt.title('Histogram of Normal Distribution Sample')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    if save_plots:
        plt.savefig('histogram.png')
        plt.close()
    
    # Create a QQ plot
    plt.figure(figsize=(10, 6))
    stats.probplot(sample, dist="norm", plot=plt)
    plt.title('QQ Plot of Normal Distribution Sample')
    if save_plots:
        plt.savefig('qq_plot.png')
        plt.close()
    
    # Return the results
    plot_paths = ['histogram.png', 'qq_plot.png'] if save_plots else []
    return skewness, kurtosis, plot_paths