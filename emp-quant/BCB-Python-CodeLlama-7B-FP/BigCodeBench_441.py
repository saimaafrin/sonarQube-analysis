import numpy as np
import matplotlib.pyplot as plt
def task_func(P, T):
    """
    Calculate the product of a matrix "P" and a 3D tensor "T" with numpy and then visualize the result in 3D with matplotlib.
    The product of the matrix and tensor is based on the Einstein summation.
    """
    # Calculate the product of the matrix and tensor
    result = np.einsum('ij,ijk->k', P, T)

    # Create a 3D visualization of the result
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(result[:, 0], result[:, 1], result[:, 2], cmap='viridis')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

    return result, ax
P = np.array([[1, 2], [3, 4]])
T = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])