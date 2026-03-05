import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
def task_func(mu, sigma, seed=0):
    np.random.seed(seed)
    x = np.random.normal(mu, sigma, 1000)
    sns.distplot(x, color="blue", kde=False, rug=True)
    ax = plt.gca()
    ax.set_title(f"Normal Distribution with mean {mu} and standard deviation {sigma}")
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    return ax
mu = 0
sigma = 1