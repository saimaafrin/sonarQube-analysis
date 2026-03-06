
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def task_func(mu=0, sigma=1):
    # Create an array of 100 linearly spaced numbers between mu - 3*sigma and mu + 3*sigma
    x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)

    # Calculate the normal distribution at each point in the array
    y = norm.pdf(x, mu, sigma)

    # Create a subplot of the normal distribution
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel('X')
    ax.set_ylabel('Probability Density')
    ax.set_title('Normal Distribution with Mean = {}, Standard Deviation = {}'.format(mu, sigma))

    return ax