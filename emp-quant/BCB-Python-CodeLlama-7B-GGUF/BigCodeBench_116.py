
import numpy as np
import matplotlib.pyplot as plt

def task_func(mu, sigma, sample_size):
    # Generate a numpy array of random samples drawn from a normal distribution
    samples = np.random.normal(mu, sigma, size=sample_size)

    # Plot the histogram of the generated samples
    plt.hist(samples, bins=30, alpha=0.75, color='blue')
    plt.xlabel('Sample values')
    plt.ylabel('Frequency')
    plt.title('Histogram of Generated Samples')
    plt.show()

    return samples