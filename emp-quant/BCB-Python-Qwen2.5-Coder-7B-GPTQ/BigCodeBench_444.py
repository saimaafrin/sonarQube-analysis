import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def task_func(n_points=100, random_seed=None):
    if random_seed is not None:
        np.random.seed(random_seed)
    
    # Generate random 3D points
    points = np.random.rand(n_points, 3)
    
    # Create a 3D scatter plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(points[:, 0], points[:, 1], points[:, 2])
    
    return points, ax