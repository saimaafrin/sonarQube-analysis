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
    features : list of str, optional
        The labels for the x-axis of the heatmap.
    seed : int, optional
        The random seed to use for shuffling.

    Returns
    -------
    Axes
        The matplotlib Axes object containing the heatmap.

    Raises
    ------
    ValueError
        If 'features' is provided and does not match the number of columns in 'array';
        and if 'array' is empty or not 2-dimensional.
    """
    if not isinstance(array, np.ndarray) or array.ndim != 2:
        raise ValueError("'array' must be a 2D numpy array.")
    if features is not None and len(features) != array.shape[1]:
        raise ValueError("'features' must have the same length as the number of columns in 'array'.")
    if seed is not None:
        np.random.seed(seed)
    shuffled_array = np.random.permutation(array)
    sns.heatmap(shuffled_array, annot=True, cmap="viridis")
    plt.show()
    return plt.gca()
array = np.array([[1, 2, 3], [4, 5, 6]])
features = ["a", "b", "c"]
seed = 42