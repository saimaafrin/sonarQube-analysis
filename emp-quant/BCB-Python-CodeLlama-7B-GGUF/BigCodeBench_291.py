
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def task_func(mu, sigma, seed=0):
    np.random.seed(seed)
    x = np.random.normal(mu, sigma, 1000)
    sns.distplot(x, hist=False, color='blue', kde=True, label='Normal distribution')
    plt.axvline(mu, color='red', label='Mean')
    plt.axvline(mu + sigma, color='green', label='Mean + 1 standard deviation')
    plt.axvline(mu - sigma, color='green', label='Mean - 1 standard deviation')
    plt.legend()
    plt.show()

task_func(0, 1)