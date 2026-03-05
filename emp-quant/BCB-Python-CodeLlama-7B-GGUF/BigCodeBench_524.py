
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt

def task_func(data):
    if not data:
        raise ValueError("Input data is empty")
    if not all(isinstance(d, dict) and all(isinstance(v, (int, float)) for v in d.values()) for d in data):
        raise TypeError("Input is not a list of dictionaries or if any value in the dictionaries is not numeric")

    means = defaultdict(list)
    stds = defaultdict(list)
    for d in data:
        for k, v in d.items():
            means[k].append(v)
            stds[k].append(np.std(v))

    fig, axs = plt.subplots(nrows=len(means), ncols=2, figsize=(15, 10))
    for i, (k, v) in enumerate(means.items()):
        axs[i, 0].bar(range(len(v)), v)
        axs[i, 1].bar(range(len(v)), stds[k])

    return (means, stds), axs