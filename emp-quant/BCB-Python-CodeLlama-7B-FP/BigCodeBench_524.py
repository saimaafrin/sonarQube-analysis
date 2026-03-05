from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt
def task_func(data):
    """
    Calculate statistical measurements (mean and standard deviation) of the values associated with each key in a list of dictionaries, and visualize mean and standard deviation with bar charts.
    The function should raise the exception for:
        ValueError: If the input data is empty.
        TypeError: If the input is not a list of dictionaries or if any value in the dictionaries is not numeric.
    The function should output with:
        tuple:
            dict: A dictionary with keys and their corresponding mean and standard deviation.
            list: A list of matplotlib Axes objects for each key's visualization.
    """
    if not data:
        raise ValueError("Input data is empty.")
    if not all(isinstance(d, dict) for d in data):
        raise TypeError("Input is not a list of dictionaries.")
    if not all(all(isinstance(v, (int, float)) for v in d.values()) for d in data):
        raise TypeError("Input contains non-numeric values.")

    # Calculate mean and standard deviation for each key
    means = defaultdict(list)
    stds = defaultdict(list)
    for d in data:
        for k, v in d.items():
            means[k].append(np.mean(v))
            stds[k].append(np.std(v))

    # Visualize mean and standard deviation for each key
    fig, axs = plt.subplots(len(means), 1, figsize=(10, 10))
    for i, (k, v) in enumerate(means.items()):
        axs[i].bar(v, label=f"Mean of {k}")
        axs[i].bar(stds[k], label=f"Standard Deviation of {k}")
        axs[i].set_title(f"Mean and Standard Deviation of {k}")
        axs[i].legend()
    return means, axs
data = [
    {"a": [1, 2, 3], "b": [4, 5, 6]},
    {"a": [7, 8, 9], "b": [10, 11, 12]},
]