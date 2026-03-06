
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def task_func(mu, sigma, seed=0):
    # Generate 1000 samples from a normal distribution with mean mu and standard deviation sigma
    np.random.seed(seed)
    samples = np.random.normal(mu, sigma, 1000)

    # Create a figure and axis object
    fig, ax = plt.subplots()

    # Plot the distribution using a histogram
    ax.hist(samples, bins=50, color='blue', alpha=0.5, label='Normal distribution')

    # Add a color bar to the plot
    cbar = ax.figure.colorbar(ax.images[0])
    cbar.ax.set_ylabel('Probability density')

    # Set the title and labels
    ax.set_title(f'Normal distribution with mean {mu} and standard deviation {sigma}')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')

    # Return the Axes object
    return ax