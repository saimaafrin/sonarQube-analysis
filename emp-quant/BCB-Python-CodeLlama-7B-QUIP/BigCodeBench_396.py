
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def task_func(mu, sigma, sample_size, seed=0):
    # Generate a random sample of size sample_size from a normal distribution with mean mu and standard deviation sigma
    random_sample = np.random.normal(mu, sigma, sample_size)

    # Compute the histogram of the sample
    hist, _ = np.histogram(random_sample, bins=50)

    # Plot the histogram
    fig, ax = plt.subplots()
    ax.plot(hist)

    return ax