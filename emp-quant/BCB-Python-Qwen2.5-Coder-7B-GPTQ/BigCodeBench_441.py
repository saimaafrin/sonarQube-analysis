import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def task_func(P, T):
    """
    Calculate the product of a matrix P and a 3D tensor T with numpy and then visualize the result in 3D with matplotlib.
    
    Args:
    P (numpy.ndarray): A 2D numpy array representing the matrix.
    T (numpy.ndarray): A 3D numpy array representing the tensor.
    
    Returns:
    tuple:
    result (numpy.ndarray): The product of matrix P and tensor T with shape (N, 3).
    ax (mpl_toolkits.mplot3d.axes3d.Axes3D): The 3D visualization of the result.
    """
    # Calculate the product using Einstein summation
    result = np.einsum('ij, jkl -> ik', P, T)
    
    # Create a 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot the result
    ax.scatter(result[:, 0], result[:, 1], result[:, 2])
    
    return result, ax
P = np.array([[1, 2], [3, 4]])
T = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])