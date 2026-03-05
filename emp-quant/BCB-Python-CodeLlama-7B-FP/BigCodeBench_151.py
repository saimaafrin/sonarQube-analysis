import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
def task_func(data_dict, data_keys):
    """
    Normalize data specified by keys in a dictionary using MinMax scaling and plot the results.
    This function is useful for preprocessing data for machine learning models where data scaling can impact performance.
    The function should raise the exception for: ValueError: If no keys in `data_keys` are found in `data_dict`.
    The function should output with:
        tuple: A tuple containing a DataFrame of normalized values and a matplotlib Axes object representing a plot of the
        normalized data.
    """
    # Check if all keys in data_keys are present in data_dict
    if not all(key in data_dict for key in data_keys):
        raise ValueError("No keys in `data_keys` are found in `data_dict`.")

    # Create a DataFrame of normalized values
    normalized_data = pd.DataFrame(index=data_dict.index, columns=data_keys)
    for key in data_keys:
        normalized_data[key] = MinMaxScaler().fit_transform(data_dict[key].values.reshape(-1, 1))

    # Create a plot of the normalized data
    fig, ax = plt.subplots()
    for key in data_keys:
        ax.plot(normalized_data[key], label=key)
    ax.set_xlabel("Normalized data")
    ax.set_ylabel("Value")
    ax.legend()

    return normalized_data, ax
data_dict = {"a": [1, 2, 3, 4, 5], "b": [2, 4, 6, 8, 10], "c": [3, 6, 9, 12, 15]}
data_keys = ["a", "b", "c"]