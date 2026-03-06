
import matplotlib.pyplot as plt
import numpy as np

def task_func(n, seed=0):
    np.random.seed(seed)
    x = np.random.rand(n)
    y = np.random.rand(n)
    points = list(zip(x, y))
    fig, ax = plt.subplots()
    ax.scatter(x, y, c='blue')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Scatter plot of random points')
    return fig, points