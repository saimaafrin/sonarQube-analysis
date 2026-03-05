
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def task_func(l):
    # Calculate the histogram of the given array
    n, bins, patches = plt.hist(l, 50, density=True, facecolor='g', alpha=0.75)

    # Calculate the Gaussian fit
    mu, sigma = stats.norm.fit(l)

    # Print the fit results
    print("Fit results: mu = {:.2f}, std = {:.2f}".format(mu, sigma))

    # Add a vertical line to the plot at the mean position
    plt.axvline(x=mu, color='r', linestyle='--')

    # Add a text label to the plot with the fit results
    plt.text(mu, 0.95, "mu = {:.2f}, std = {:.2f}".format(mu, sigma), fontsize=12)

    # Set the title of the plot
    plt.title("Histogram of the given array with a Gaussian fit")

    # Return the Axes object with the plot
    return plt.gca()

# Show the plot
plt.show()