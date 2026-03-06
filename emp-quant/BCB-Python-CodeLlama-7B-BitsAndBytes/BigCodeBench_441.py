
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def task_func(P, T):
    # Calculate the product of the matrix and tensor
    result = np.einsum('ij,ijk->k', P, T)

    # Create a 3D visualization of the result
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(result[:,0], result[:,1], result[:,2], c=result)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Product of Matrix and Tensor')

    return result, ax

# Visualize the result
plt.show()