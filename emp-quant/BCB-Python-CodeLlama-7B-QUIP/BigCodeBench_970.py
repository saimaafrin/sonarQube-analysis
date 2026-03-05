
import numpy as np
import matplotlib.pyplot as plt

def task_func(data: np.ndarray) -> plt.Axes:
    """
    Plots the cumulative probability distribution of a given NumPy array of numbers.
    """
    if not isinstance(data, np.ndarray):
        raise TypeError("Input must be a NumPy array.")
    if not data.size > 0:
        raise ValueError("Input array must contain at least one element.")
    if np.any(data < 0) or np.any(np.isnan(data)):
        raise ValueError("Input array cannot contain negative numbers or NaNs.")

    # Sort the data in ascending order
    sorted_data = np.sort(data)

    # Calculate the cumulative probability
    cumulative_prob = np.cumsum(sorted_data)

    # Plot the cumulative probability curve
    fig, ax = plt.subplots()
    ax.plot(cumulative_prob, marker='o', ls='-')
    ax.set_xlabel("Index")
    ax.set_ylabel("Cumulative Probability")
    ax.set_title("Cumulative Probability Plot")
    return ax