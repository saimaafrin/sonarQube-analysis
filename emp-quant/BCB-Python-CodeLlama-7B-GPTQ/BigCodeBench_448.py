import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
def task_func(mu=0, sigma=1):
    """
    Draw and return a subplot of a normal distribution with the given mean and standard deviation, utilizing numpy's linspace to create an array of 100 linearly spaced numbers between mu - 3*sigma and mu + 3*sigma.
    """
    x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
    y = norm.pdf(x, mu, sigma)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Normal Distribution')
    return ax
mu = 0
sigma = 1