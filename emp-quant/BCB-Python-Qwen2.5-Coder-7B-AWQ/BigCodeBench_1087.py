import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
def task_func(mean=123456.908, std_dev=1.2, save_plots=False):
    # Generate a random sample from a normal distribution
    sample = np.random.normal(mean, std_dev, 1000)
    
    # Analyze its skewness and kurtosis
    skewness = stats.skew(sample)
    kurtosis = stats.kurtosis(sample)
    
    # Create a histogram and a QQ plot to visualize the distribution
    if save_plots:
        plt.figure(figsize=(12, 6))
        plt.subplot(1, 2, 1)
        plt.hist(sample, bins=30, density=True, alpha=0.6, color='g')
        plt.title('Histogram of the Sample')
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        
        plt.subplot(1, 2, 2)
        stats.probplot(sample, dist="norm", plot=plt)
        plt.title('QQ Plot of the Sample')
        plt.xlabel('Theoretical Quantiles')
        plt.ylabel('Sample Quantiles')
        
        # Save the plots
        plt.savefig('histogram.png')
        plt.savefig('qq_plot.png')
        plot_paths = ['histogram.png', 'qq_plot.png']
    else:
        plot_paths = []
    
    return skewness, kurtosis, plot_paths