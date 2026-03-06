
import numpy as np
import matplotlib.pyplot as plt

def task_func(mu, sigma, sample_size):
    """
    Generates a numpy array of random samples drawn from a normal distribution and plots the histogram of these samples.

    Parameters:
    mu (float): The mean of the normal distribution.
    sigma (float): The standard deviation of the normal distribution.
    sample_size (int): The number of samples to generate.

    Returns:
    ndarray: A numpy array of shape (sample_size,) containing samples drawn from the specified normal distribution.
    """
    # Generate samples from a normal distribution
    samples = np.random.normal(mu, sigma, sample_size)
    
    # Plotting the histogram
    plt.figure(figsize=(10, 6))
    plt.hist(samples, bins=30, alpha=0.75, color='blue')
    plt.title('Histogram of Generated Samples')
    plt.xlabel('Sample values')
    plt.ylabel('Frequency')
    plt.show()
    
    return samples