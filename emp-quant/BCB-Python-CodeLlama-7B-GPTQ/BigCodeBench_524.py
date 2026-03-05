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
    # Check if the input data is empty
    if not data:
        raise ValueError("Input data is empty.")

    # Check if the input is a list of dictionaries
    if not isinstance(data, list) or not all(isinstance(d, dict) for d in data):
        raise TypeError("Input is not a list of dictionaries.")

    # Check if all values in the dictionaries are numeric
    if not all(all(isinstance(v, (int, float)) for v in d.values()) for d in data):
        raise TypeError("Not all values in the dictionaries are numeric.")

    # Calculate the mean and standard deviation for each key
    means = defaultdict(list)
    stds = defaultdict(list)
    for d in data:
        for k, v in d.items():
            means[k].append(v)
            stds[k].append(np.std(v))

    # Visualize the mean and standard deviation for each key
    fig, axs = plt.subplots(len(means), 1, figsize=(10, 6))
    for i, (k, v) in enumerate(means.items()):
        axs[i].bar(v, label=f"Mean: {np.mean(v):.2f}")
        axs[i].bar(v, label=f"Standard Deviation: {stds[k][0]:.2f}")
        axs[i].set_title(f"Mean and Standard Deviation for {k}")
        axs[i].legend()

    return means, axs
data = [
    {"a": 1, "b": 2, "c": 3},
    {"a": 4, "b": 5, "c": 6},
    {"a": 7, "b": 8, "c": 9},
]