
import matplotlib.pyplot as plt
import numpy as np

def task_func(n, seed=0):
    np.random.seed(seed)
    x = np.random.uniform(0, 10, n)
    y = np.random.uniform(0, 10, n)
    points = list(zip(x, y))
    fig, ax = plt.subplots()
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.scatter(x, y)
    ax.set_title('Scatter plot of random points')
    return fig, points