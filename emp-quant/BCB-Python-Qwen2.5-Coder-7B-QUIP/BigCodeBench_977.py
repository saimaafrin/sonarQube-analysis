
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def task_func(array, features=None, seed=None):
    """
    Shuffles the columns of a given 2D numpy array and visualizes it as a heatmap.
    
    Parameters:
    array (numpy.ndarray): A 2D numpy array to shuffle and visualize.
    features (list, optional): A list of strings to use as labels for the heatmap's x-axis. Defaults to None.
    seed (int, optional): A seed for the random number generator for reproducibility. Defaults to None.
    
    Returns:
    Axes: The matplotlib Axes object containing the heatmap.
    
    Raises:
    ValueError: If 'features' is provided and does not match the number of columns in 'array'.
    ValueError: If 'array' is empty or not 2-dimensional.
    """
    if not array or not isinstance(array, np.ndarray) or array.ndim != 2:
        raise ValueError("Input 'array' must be a non-empty 2D numpy array.")
    
    if features and len(features) != array.shape[1]:
        raise ValueError("Length of 'features' must match the number of columns in 'array'.")
    
    if seed is not None:
        np.random.seed(seed)
    
    # Shuffle the columns of the array
    shuffled_array = np.random.permutation(array.T).T
    
    # Get the column labels
    if features:
        labels = features
    else:
        labels = [f"col{i+1}" for i in range(array.shape[1])]
    
    # Create the heatmap
    fig, ax = plt.subplots()
    sns.heatmap(shuffled_array, annot=True, cmap='viridis', ax=ax)
    ax.set_xlabel('Columns')
    ax.set_ylabel('Rows')
    ax.set_xticklabels(labels, rotation=90)
    
    return ax