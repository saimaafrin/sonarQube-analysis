
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def task_func(array, features=None, seed=None):
    if not isinstance(array, np.ndarray):
        raise ValueError("'array' must be a 2D numpy array")
    if array.ndim != 2:
        raise ValueError("'array' must be a 2D numpy array")
    if array.size == 0:
        raise ValueError("'array' cannot be empty")
    if features is not None:
        if len(features) != array.shape[1]:
            raise ValueError("'features' must have the same number of elements as the number of columns in 'array'")
    if seed is not None:
        np.random.seed(seed)
    shuffled_array = np.random.permutation(array)
    if features is not None:
        x_labels = features
    else:
        x_labels = [str(i) for i in range(1, array.shape[1] + 1)]
    sns.heatmap(shuffled_array, annot=True, cmap="coolwarm", xticklabels=x_labels)
    plt.show()
    return plt.gca()