
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def task_func(array, features=None, seed=None):
    """
    Shuffles the columns of a given 2D numpy array and visualizes it as a heatmap.

    Parameters:
    - array (np.ndarray): A 2D numpy array to be shuffled and visualized.
    - features (list, optional): A list of feature names to use as labels for the heatmap's x-axis.
    - seed (int, optional): Seed for random number generator for reproducibility.

    Returns:
    - Axes: The matplotlib Axes object containing the heatmap.

    Raises:
    - ValueError: If 'features' is provided and does not match the number of columns in 'array'.
    - ValueError: If 'array' is empty or not 2-dimensional.
    """

    # Check if array is empty or not 2-dimensional
    if array.size == 0 or len(array.shape) != 2:
        raise ValueError("Input array must be non-empty and 2-dimensional.")

    # Shuffle columns
    if seed is not None:
        np.random.seed(seed)
    shuffled_indices = np.random.permutation(array.shape[1])
    shuffled_array = array[:, shuffled_indices]

    # Set default features if none are provided
    if features is None:
        features = [f"Feature {i+1}" for i in range(shuffled_array.shape[1])]

    # Check if features match the number of columns
    if len(features) != shuffled_array.shape[1]:
        raise ValueError("Number of features must match the number of columns in the array.")

    # Create heatmap
    fig, ax = plt.subplots()
    sns.heatmap(shuffled_array, annot=False, cmap='viridis', xticklabels=features, yticklabels=False, ax=ax)

    return ax