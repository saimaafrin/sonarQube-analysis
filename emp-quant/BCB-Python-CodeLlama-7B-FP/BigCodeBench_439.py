import numpy as np
import seaborn as sns
def task_func(P, T):
    """
    Calculate the product of a matrix 'P' and a 3D tensor 'T' using numpy and visualize the results as a heatmap.
    """
    # Calculate the product of the matrix and the tensor
    result = np.matmul(P, T)

    # Reshape the result into a 2D array
    result_2d = result.reshape(result.shape[0], -1)

    # Visualize the heatmap
    fig, ax = plt.subplots()
    sns.heatmap(result_2d, annot=True, cmap="YlGnBu")

    return result, ax
P = np.array([[1, 2], [3, 4]])
T = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])