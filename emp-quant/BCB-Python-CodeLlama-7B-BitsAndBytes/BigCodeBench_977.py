
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def task_func(array, features=None, seed=None):
    # Check if array is empty or not 2-dimensional
    if array.size == 0 or array.ndim != 2:
        raise ValueError("'array' must be a non-empty 2-dimensional numpy array")

    # Check if 'features' is provided and matches the number of columns in 'array'
    if features is not None and features.size != array.shape[1]:
        raise ValueError("'features' must be None or have the same number of elements as the number of columns in 'array'")

    # Shuffle the columns of the array
    if seed is not None:
        np.random.seed(seed)
    shuffled_array = np.random.permutation(array.T)

    # Create a heatmap of the shuffled array
    fig, ax = plt.subplots()
    sns.heatmap(shuffled_array, annot=True, cmap="coolwarm")
    ax.set_title("Shuffled Array")
    ax.set_xlabel("Features" if features is not None else "Numerical Labels")
    ax.set_ylabel("Rows")
    plt.show()

    return ax