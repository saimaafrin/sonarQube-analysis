import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
def task_func(mu, sigma, seed=0):
    np.random.seed(seed)
    x = np.random.normal(mu, sigma, 1000)
    sns.distplot(x, hist=False, kde=True, color="blue")
    plt.axvline(mu, color="red", label="mean")
    plt.axvline(mu + sigma, color="green", label="mean + 1 std")
    plt.axvline(mu - sigma, color="green", label="mean - 1 std")
    plt.legend()
    return plt.gca()
mu = 0
sigma = 1