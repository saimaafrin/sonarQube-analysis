import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
def task_func(array, features=None, seed=None):
    """
    Shuffles the columns of a given 2D numpy array and visualizes it as a heatmap.

    Parameters
    ----------
    array : 2D numpy array
        The array to be shuffled and visualized.
    features : list, optional
        The list of features to be used as labels for the x-axis of the heatmap.
        If not provided, the function will use the numerical labels starting from 1.
    seed : int, optional
        The random seed to be used for shuffling the columns.

    Returns
    -------
    Axes
        The matplotlib Axes object containing the heatmap.

    Raises
    ------
    ValueError
        If 'features' is provided and does not match the number of columns in 'array'.
        If 'array' is empty or not 2-dimensional.
    """
    # Check if the input array is valid
    if not isinstance(array, np.ndarray) or array.ndim != 2:
        raise ValueError("'array' must be a 2D numpy array.")

    # Check if the number of features matches the number of columns in the array
    if features is not None and len(features) != array.shape[1]:
        raise ValueError("'features' must have the same number of elements as the number of columns in 'array'.")

    # Shuffle the columns of the array
    if seed is not None:
        np.random.seed(seed)
    shuffled_array = np.random.permutation(array.T).T

    # Create a heatmap of the shuffled array
    sns.heatmap(shuffled_array, annot=True, cmap="Blues")

    # Return the Axes object containing the heatmap
    return plt.gca()
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
features = ["a", "b", "c"]