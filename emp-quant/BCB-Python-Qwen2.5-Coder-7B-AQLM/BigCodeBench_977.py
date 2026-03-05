
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def task_func(array, features=None, seed=None):
    """
    Shuffles the columns of a given 2D numpy array and visualizes it as a heatmap.
    
    Parameters:
    - array: 2D numpy array to be shuffled and visualized.
    - features: Optional list of strings to use as labels for the heatmap's x-axis.
    - seed: Optional integer to set the random seed for reproducibility.
    
    Returns:
    - Axes: The matplotlib Axes object containing the heatmap.
    
    Raises:
    - ValueError: If 'features' is provided and does not match the number of columns in 'array';
      or if 'array' is empty or not 2-dimensional.
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
    
    # Create a figure and axis for the heatmap
    fig, ax = plt.subplots()
    
    # Create the heatmap
    sns.heatmap(shuffled_array, annot=True, fmt=".2f", cmap='viridis', ax=ax)
    
    # Set the x-axis labels
    if features is not None:
        ax.set_xticks(np.arange(len(features)))
        ax.set_xticklabels(features)
    else:
        ax.set_xticks(np.arange(1, shuffled_array.shape[1] + 1))
        ax.set_xticklabels([str(i) for i in range(1, shuffled_array.shape[1] + 1)])
    
    # Return the Axes object
    return ax