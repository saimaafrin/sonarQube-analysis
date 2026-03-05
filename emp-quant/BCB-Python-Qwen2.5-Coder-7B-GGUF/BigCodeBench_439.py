
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(P, T):
    """
    Multiplies a matrix P with a 3D tensor T and returns the result as a 2D numpy array.
    Also, it visualizes the 2D result as a heatmap.
    
    Parameters:
    P (numpy.ndarray): A 2D numpy array representing the matrix.
    T (numpy.ndarray): A 3D numpy array representing the tensor.
    
    Returns:
    numpy.ndarray: The 2D result of the matrix-tensor multiplication.
    matplotlib.axes.Axes: The axes object of the heatmap.
    """
    # Ensure P is a 2D array and T is a 3D array
    if P.ndim != 2 or T.ndim != 3:
        raise ValueError("P must be a 2D array and T must be a 3D array.")
    
    # Perform matrix-tensor multiplication
    result = np.einsum('ij, jkl -> ikl', P, T)
    
    # Flatten the result to 2D for heatmap visualization
    heatmap_data = result.sum(axis=2)
    
    # Create a heatmap
    ax = sns.heatmap(heatmap_data, annot=True, fmt=".2f", cmap='viridis')
    
    # Return the result and the axes object
    return result, ax