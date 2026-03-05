
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def task_func(array, features=None, seed=None):
    if not isinstance(array, np.ndarray):
        raise ValueError("'array' must be a numpy array")
    if array.ndim != 2:
        raise ValueError("'array' must be a 2-dimensional numpy array")
    if features is not None:
        if len(features) != array.shape[1]:
            raise ValueError("'features' must have the same number of elements as the number of columns in 'array'")
    if seed is not None:
        np.random.seed(seed)
    shuffled_array = np.random.permutation(array)
    if features is not None:
        features = features[shuffled_array]
    else:
        features = [str(i) for i in range(1, shuffled_array.shape[1] + 1)]
    fig, ax = plt.subplots()
    sns.heatmap(shuffled_array, ax=ax, cbar_format="%1.2f", cbar_ax=False)
    ax.set_xticks(np.arange(0, shuffled_array.shape[1], 1))
    ax.set_xticklabels(features)
    ax.set_xlabel("Features")
    ax.set_ylabel("Values")
    return ax