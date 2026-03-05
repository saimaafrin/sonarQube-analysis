import random
import matplotlib.pyplot as plt
DISTRIBUTION_SIZE = 1000
def task_func(bins=30):
    # Generate Gaussian distribution
    distribution = [random.gauss(0, 1) for _ in range(DISTRIBUTION_SIZE)]
    
    # Plot histogram
    fig, ax = plt.subplots()
    ax.hist(distribution, bins=bins, density=True)
    
    # Return the distribution list and the Axes patch object
    return distribution, ax