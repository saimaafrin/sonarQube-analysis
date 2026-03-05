import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
def task_func(P, T):
    """
    Calculate the product of a matrix 'P' and a 3D tensor 'T' using numpy and visualize the results as a heatmap.
    
    Args:
    P (numpy.ndarray): A 2D numpy array representing the matrix.
    T (numpy.ndarray): A 3D numpy array representing the tensor.
    
    Returns:
    numpy.ndarray: Resultant product after matrix-tensor multiplication.
    matplotlib.axes.Axes: Axes object displaying the heatmap of the 2D result.
    """
    # Ensure P is a 2D array and T is a 3D array
    if P.ndim != 2 or T.ndim != 3:
        raise ValueError("P must be a 2D array and T must be a 3D array.")
    
    # Perform matrix-tensor multiplication
    result = np.einsum('ij, jkl -> ikl', P, T)
    
    # Flatten the result to create a 2D array for heatmap visualization
    result_2d = result.flatten()
    
    # Create a heatmap using seaborn
    ax = sns.heatmap(result_2d.reshape(1, -1), annot=True, fmt=".2f", cmap='viridis')
    
    # Return the result and the axes object
    return result, ax
P = np.array([[1, 2], [3, 4]])
T = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])