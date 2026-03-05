
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def task_func(mu, sigma, num_samples=1000, seed=77):
    np.random.seed(seed)
    samples = np.random.normal(mu, sigma, num_samples)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    
    # Histogram
    ax1.hist(samples, bins=30, density=True, alpha=0.6, color='g')
    ax1.set_title('Histogram of Normal Distribution')
    ax1.set_xlabel('Value')
    ax1.set_ylabel('Density')
    
    # Q-Q plot
    stats.probplot(samples, dist="norm", plot=ax2)
    ax2.set_title('Q-Q Plot of Normal Distribution')
    ax2.set_xlabel('Theoretical Quantiles')
    ax2.set_ylabel('Sample Quantiles')
    
    return fig