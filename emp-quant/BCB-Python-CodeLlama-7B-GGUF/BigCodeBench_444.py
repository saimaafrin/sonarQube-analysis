
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def task_func(n_points=100, random_seed=None):
    if random_seed is not None:
        np.random.seed(random_seed)

    points = np.random.rand(n_points, 3)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], c='b')

    return (points, ax)