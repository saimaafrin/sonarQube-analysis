import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
def task_func(P, T):
    """
    Multiplies a matrix 'P' with a 3D tensor 'T' and returns the result as a numpy array.
    Also, it visualizes the 2D result as a heatmap.
    
    Parameters:
    - P: numpy.ndarray, a 2D matrix.
    - T: numpy.ndarray, a 3D tensor.
    
    Returns:
    - numpy.ndarray: The result of the matrix-tensor multiplication.
    - matplotlib.axes.Axes: The axes object of the heatmap.
    """
    # Perform matrix-tensor multiplication
    result = np.einsum('ij,klm->iklm', P, T)
    
    # Flatten the result to 2D for heatmap visualization
    heatmap_data = result.sum(axis=2)
    
    # Create a heatmap
    ax = sns.heatmap(heatmap_data, annot=True, fmt=".2f", cmap='viridis')
    
    return result, ax
P = np.array([[1, 2], [3, 4]])
T = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])