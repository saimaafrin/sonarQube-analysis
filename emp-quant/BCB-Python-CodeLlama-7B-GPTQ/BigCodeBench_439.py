import numpy as np
import seaborn as sns
def task_func(P, T):
    """
    Calculate the product of a matrix 'P' and a 3D tensor 'T' using numpy and visualize the results as a heatmap.
    Note that: This function only accepts numpy matrices/arrays.
    The function should output with:
        numpy.ndarray: Resultant product after matrix-tensor multiplication.
        matplotlib.axes.Axes: Axes object displaying the heatmap of the 2D result.
    """
    # Calculate the product of the matrix and the tensor
    result = np.matmul(P, T)

    # Reshape the result into a 2D array
    result_2d = result.reshape((result.shape[0], -1))

    # Visualize the heatmap of the 2D result
    fig, ax = plt.subplots()
    sns.heatmap(result_2d, ax=ax, cmap="viridis")

    return result, ax
P = np.array([[1, 2], [3, 4]])
T = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])