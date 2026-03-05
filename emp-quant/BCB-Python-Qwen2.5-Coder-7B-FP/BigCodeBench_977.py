import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
def task_func(array, features=None, seed=None):
    """
    Shuffles the columns of a given 2D numpy array and visualizes it as a heatmap.
    
    Parameters:
    - array: 2D numpy array to shuffle and visualize.
    - features: List of strings to use as labels for the heatmap's x-axis. If None, uses numerical labels.
    - seed: Integer to set the random seed for reproducibility.
    
    Returns:
    - Axes: The matplotlib Axes object containing the heatmap.
    """
    # Check if the array is empty or not 2-dimensional
    if array.size == 0 or array.ndim != 2:
        raise ValueError("The array must be non-empty and 2-dimensional.")
    
    # Check if features are provided and match the number of columns
    if features is not None and len(features) != array.shape[1]:
        raise ValueError("The number of features must match the number of columns in the array.")
    
    # Set the random seed if provided
    if seed is not None:
        np.random.seed(seed)
    
    # Shuffle the columns of the array
    shuffled_array = array[:, np.random.permutation(array.shape[1])]
    
    # Create a list of default features if none are provided
    if features is None:
        features = [str(i) for i in range(1, array.shape[1] + 1)]
    
    # Create a heatmap using seaborn
    ax = sns.heatmap(shuffled_array, xticklabels=features, cmap='viridis')
    
    # Return the Axes object
    return ax