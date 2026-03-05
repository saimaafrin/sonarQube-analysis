import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
def task_func(array, features=None, seed=None):
    """
    Shuffles the columns of a given 2D numpy array and visualizes it as a heatmap.
    
    Parameters:
    - array: 2D numpy array to be shuffled and visualized.
    - features: List of strings to be used as labels for the heatmap's x-axis.
    - seed: Integer to be used as the seed for the random number generator.
    
    Returns:
    - Axes: The matplotlib Axes object containing the heatmap.
    """
    # Check if the array is empty or not 2-dimensional
    if array.size == 0 or array.ndim != 2:
        raise ValueError("The array must be non-empty and 2-dimensional.")
    
    # Check if features are provided and match the number of columns
    if features is not None and len(features) != array.shape[1]:
        raise ValueError("The number of features must match the number of columns in the array.")
    
    # Shuffle the columns of the array
    if seed is not None:
        np.random.seed(seed)
    shuffled_array = array[:, np.random.permutation(array.shape[1])]
    
    # Create labels for the x-axis
    if features is not None:
        x_labels = features
    else:
        x_labels = [str(i) for i in range(1, array.shape[1] + 1)]
    
    # Create a heatmap using seaborn
    plt.figure(figsize=(10, 6))
    heatmap = sns.heatmap(shuffled_array, annot=True, fmt=".2f", cmap="YlGnBu", xticklabels=x_labels)
    plt.show()
    
    return heatmap
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
features = ['A', 'B', 'C']
seed = 42