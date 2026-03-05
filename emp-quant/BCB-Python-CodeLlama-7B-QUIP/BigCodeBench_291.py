
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def task_func(mu, sigma, seed=0):
    np.random.seed(seed)
    x = np.random.normal(mu, sigma, 1000)
    fig, ax = plt.subplots()
    ax.hist(x, bins=50, alpha=0.5, label="Normal distribution")
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    ax.set_title("Normal distribution with mean = %s and std = %s" % (mu, sigma))
    ax.set_xticks(np.linspace(0, 10, 100))
    ax.set_xticklabels(np.linspace(0, 10, 100))
    ax.set_yticks(np.linspace(0, 100, 10))
    ax.set_yticklabels(np.linspace(0, 100, 10))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 100)
    ax.legend()
    return ax