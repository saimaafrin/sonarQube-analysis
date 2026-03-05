
import matplotlib.pyplot as plt
import numpy as np

def task_func(n, seed=0):
    np.random.seed(seed)
    x = np.random.rand(n)
    y = np.random.rand(n)
    points = [(x[i], y[i]) for i in range(n)]
    fig = plt.figure(figsize=(8, 8))
    plt.scatter(x, y, c='b', alpha=0.5)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Scatter plot of random points')
    return fig, points