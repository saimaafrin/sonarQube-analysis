
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def task_func(array, features=None, seed=None):
    """
    Shuffles the columns of a given 2D numpy array and visualizes it as a heatmap.
    
    Parameters:
    - array: 2D numpy array to be shuffled and visualized.
    - features: List of strings to be used as labels for the heatmap's x-axis. If None, uses numerical labels.
    - seed: Integer to set the random seed for reproducibility.
    
    Returns:
    - Axes: The matplotlib Axes object containing the heatmap.
    
    Raises:
    - ValueError: If 'features' is provided and does not match the number of columns in 'array'; or if 'array' is empty or not 2-dimensional.
    """
    if seed is not None:
        np.random.seed(seed)
    
    if array.ndim != 2:
        raise ValueError("The input array must be 2-dimensional.")
    if array.size == 0:
        raise ValueError("The input array cannot be empty.")
    
    if features is not None:
        if len(features) != array.shape[1]:
            raise ValueError("The length of 'features' must match the number of columns in 'array'.")
    
    # Shuffle the columns of the array
    shuffled_array = array[:, np.random.permutation(array.shape[1])]
    
    # Create a heatmap
    if features is not None:
        sns.heatmap(shuffled_array, xticklabels=features)
    else:
        sns.heatmap(shuffled_array, xticklabels=[str(i+1) for i in range(array.shape[1])])
    
    # Get the current Axes object
    ax = plt.gca()
    
    # Show the plot
    plt.show()
    
    return ax