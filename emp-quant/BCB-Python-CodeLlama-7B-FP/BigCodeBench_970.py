import numpy as np
import matplotlib.pyplot as plt
def task_func(data: np.ndarray) -> plt.Axes:
    """
    Plots the cumulative probability distribution of a given NumPy array of numbers, representing how the cumulative probability increases with the sorted data indexes.
    Note that:
        - In case of an all-zeros input, the cumulative probability remains at 0 across all indexes.
        - The plot uses marker ('o') and a solid line ('-') for the cumulative probability curve.
        - The plot is titled "Cumulative Probability Plot", with "Index" on the x-axis and "Cumulative Probability" on the y-axis.
        - The function should raise the exception for:
            - ValueError: If the input array contains negative numbers or NaNs.
            - TypeError: If the input array contains non-numeric inputs.
    """
    # Check for negative numbers or NaNs
    if np.any(data < 0) or np.any(np.isnan(data)):
        raise ValueError("Input array contains negative numbers or NaNs.")

    # Check for non-numeric inputs
    if not np.issubdtype(data.dtype, np.number):
        raise TypeError("Input array contains non-numeric inputs.")

    # Sort the data
    sorted_data = np.sort(data)

    # Calculate the cumulative probability
    cumulative_probability = np.cumsum(sorted_data) / np.sum(sorted_data)

    # Plot the cumulative probability
    fig, ax = plt.subplots()
    ax.plot(sorted_data, cumulative_probability, 'o-')
    ax.set_xlabel("Index")
    ax.set_ylabel("Cumulative Probability")
    ax.set_title("Cumulative Probability Plot")
    return ax
data = np.array([1, 2, 3, 4, 5])