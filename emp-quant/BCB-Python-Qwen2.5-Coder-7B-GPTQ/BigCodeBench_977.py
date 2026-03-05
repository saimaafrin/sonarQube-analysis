import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
def task_func(array, features=None, seed=None):
    """
    Shuffles the columns of a given 2D numpy array and visualizes it as a heatmap.
    
    Parameters:
    - array: 2D numpy array to be shuffled and visualized.
    - features: List of strings to use as labels for the heatmap's x-axis. If not provided, default labels are used.
    - seed: Integer to set the random seed for reproducibility.
    
    Returns:
    - Axes: The matplotlib Axes object containing the heatmap.
    """
    # Check if the array is empty or not 2-dimensional
    if array.size == 0 or array.ndim != 2:
        raise ValueError("The input array must be non-empty and 2-dimensional.")
    
    # Set the random seed if provided
    if seed is not None:
        np.random.seed(seed)
    
    # Shuffle the columns of the array
    shuffled_array = array[:, np.random.permutation(array.shape[1])]
    
    # Determine the x-axis labels
    if features is not None:
        if len(features) != shuffled_array.shape[1]:
            raise ValueError("The length of 'features' must match the number of columns in 'array'.")
        x_labels = features
    else:
        x_labels = [str(i) for i in range(1, shuffled_array.shape[1] + 1)]
    
    # Create a heatmap using seaborn
    plt.figure(figsize=(10, 6))
    heatmap = sns.heatmap(shuffled_array, xticklabels=x_labels, cmap='viridis')
    plt.show()
    
    return heatmap