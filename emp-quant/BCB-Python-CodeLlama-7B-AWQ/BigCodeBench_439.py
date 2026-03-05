import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
def task_func(P, T):
    """
    Calculate the product of a matrix 'P' and a 3D tensor 'T' using numpy and visualize the results as a heatmap.
    """
    # Calculate the product of the matrix and the tensor
    result = np.matmul(P, T)

    # Create a 2D array from the result
    result_2d = np.reshape(result, (result.shape[0], -1))

    # Visualize the heatmap
    fig, ax = plt.subplots()
    sns.heatmap(result_2d, ax=ax, cmap="viridis")
    ax.set_title("Heatmap of the result")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")

    return result, ax
P = np.array([[1, 2], [3, 4]])
T = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])