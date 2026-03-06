
import numpy as np
import matplotlib.pyplot as plt

def task_func(n_points=100, random_seed=None):
    # Generate random 3D points in the range [0, 1)
    points = np.random.rand(n_points, 3)

    # Create a 3D scatter plot of the points
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(points[:,0], points[:,1], points[:,2], c='r')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

    return (points, ax)