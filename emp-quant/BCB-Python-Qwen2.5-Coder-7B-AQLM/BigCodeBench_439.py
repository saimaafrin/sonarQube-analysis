
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(P, T):
    """
    Multiplies a matrix P with a 3D tensor T and returns the result as a numpy array.
    Also, it plots a heatmap of the 2D result.
    
    Parameters:
    P (numpy.ndarray): A 2D numpy array representing the matrix.
    T (numpy.ndarray): A 3D numpy array representing the tensor.
    
    Returns:
    numpy.ndarray: The 2D result of the matrix-tensor multiplication.
    matplotlib.axes.Axes: The axes object of the heatmap.
    """
    # Ensure P and T are numpy arrays
    P = np.array(P)
    T = np.array(T)
    
    # Perform matrix-tensor multiplication
    result = np.einsum('ij,klj->kli', P, T)
    
    # Plotting the heatmap
    fig, ax = plt.subplots()
    sns.heatmap(result[0], annot=True, fmt=".2f", ax=ax)
    ax.set_title('Heatmap of the Resultant 2D Array')
    
    return result, ax