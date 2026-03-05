
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def task_func(mu, sigma, num_samples):
    # Generate random samples from a normal distribution
    samples = np.random.normal(mu, sigma, num_samples)
    
    # Create a figure and axis
    fig, ax = plt.subplots()
    
    # Plot the normal distribution curve
    x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
    ax.plot(x, stats.norm.pdf(x, mu, sigma), 'r-', lw=2, label='Normal distribution')
    
    # Overlay the histogram of the samples
    ax.hist(samples, bins=30, density=True, alpha=0.6, color='g', label='Histogram')
    
    # Set the title of the plot
    ax.set_title('Normal Distribution')
    
    # Add a legend
    ax.legend()
    
    # Show the plot
    plt.show()
    
    return fig