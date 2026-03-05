import random
import matplotlib.pyplot as plt
DISTRIBUTION_SIZE = 1000
def task_func(bins=30):
    # Generate a Gaussian distribution
    distribution = [random.gauss(0, 1) for _ in range(DISTRIBUTION_SIZE)]
    
    # Plot the histogram of the distribution
    fig, ax = plt.subplots()
    ax.hist(distribution, bins=bins, density=True, alpha=0.6, color='g')
    
    # Return the distribution list and the Axes patch object
    return distribution, ax