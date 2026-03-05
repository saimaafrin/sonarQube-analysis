
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt

def task_func(data):
    if not data:
        raise ValueError("Input data is empty")
    if not all(isinstance(d, dict) for d in data):
        raise TypeError("Input is not a list of dictionaries")
    if not all(all(isinstance(v, (int, float)) for v in d.values()) for d in data):
        raise TypeError("Not all values are numeric")

    # Calculate mean and standard deviation for each key
    means = defaultdict(lambda: np.mean)
    stds = defaultdict(lambda: np.std)
    for d in data:
        for k, v in d.items():
            means[k].append(v)
            stds[k].append(v)

    # Visualize the results
    fig, axs = plt.subplots(nrows=len(means), ncols=1, figsize=(10, 10))
    for i, (k, mean, std) in enumerate(means.items()):
        axs[i].bar(mean, std)
        axs[i].set_xlabel(f"{k} mean")
        axs[i].set_ylabel(f"{k} standard deviation")
    return means, axs