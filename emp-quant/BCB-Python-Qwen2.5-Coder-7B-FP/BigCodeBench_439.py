import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
def task_func(P, T):
    """
    Multiplies a matrix 'P' with a 3D tensor 'T' and returns the result as a 2D numpy array.
    Also, it visualizes the 2D result as a heatmap.
    
    Parameters:
    - P: numpy.ndarray, a 2D matrix.
    - T: numpy.ndarray, a 3D tensor.
    
    Returns:
    - numpy.ndarray: The 2D result of the matrix-tensor multiplication.
    - matplotlib.axes.Axes: Axes object displaying the heatmap of the 2D result.
    """
    # Perform matrix-tensor multiplication
    result = np.einsum('ij, jkl -> ikl', P, T)
    
    # Flatten the result to 2D for heatmap visualization
    result_2d = result.sum(axis=2)
    
    # Create a heatmap
    ax = sns.heatmap(result_2d, annot=True, fmt=".2f", cmap='viridis')
    
    # Return the 2D result and the axes object
    return result_2d, ax