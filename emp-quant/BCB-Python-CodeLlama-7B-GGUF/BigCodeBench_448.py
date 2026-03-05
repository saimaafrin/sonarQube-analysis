
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def task_func(mu=0, sigma=1):
    # Generate an array of 100 linearly spaced numbers between mu - 3*sigma and mu + 3*sigma
    x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)

    # Calculate the corresponding normal distribution values
    y = norm.pdf(x, mu, sigma)

    # Create a subplot of the normal distribution
    ax = plt.subplot()
    ax.plot(x, y)

    return ax