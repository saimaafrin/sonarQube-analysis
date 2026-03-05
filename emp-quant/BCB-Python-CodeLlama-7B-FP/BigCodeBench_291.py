import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
def task_func(mu, sigma, seed=0):
    """
    Draw a normal distribution using a 1000 samples, indicating the mean and standard deviation with a color bar.
    """
    np.random.seed(seed)
    x = np.random.normal(mu, sigma, 1000)
    sns.distplot(x, hist=False, color="blue", label=f"Mean: {mu}, Std. Dev.: {sigma}")
    plt.legend()
    return plt.gca()
mu = 0
sigma = 1