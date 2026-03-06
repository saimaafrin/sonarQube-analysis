
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

def task_func(P, T):
    """
    Multiplies a matrix P with a 3D tensor T and returns the resultant 2D array.
    
    Parameters:
        P (numpy.ndarray): A 2D numpy array representing the matrix.
        T (numpy.ndarray): A 3D numpy array representing the tensor.
        
    Returns:
        numpy.ndarray: The 2D array resulting from the matrix-tensor multiplication.
        matplotlib.axes.Axes: The axes object containing the heatmap visualization.
    """
    # Ensure P is a 2D array and T is a 3D array
    if P.ndim != 2 or T.ndim != 3:
        raise ValueError("Input arrays must be 2D for P and 3D for T.")
    
    # Perform matrix-tensor multiplication
    result = np.tensordot(P, T, axes=1)
    
    # Create a heatmap to visualize the result
    fig, ax = plt.subplots()
    sns.heatmap(result, annot=True, fmt=".2f", cmap="YlGnBu")
    plt.show()
    
    return result, ax