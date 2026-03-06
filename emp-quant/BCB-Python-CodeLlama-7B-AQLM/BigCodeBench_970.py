import numpy as np
import matplotlib.pyplot as plt
def task_func(data: np.ndarray) -> plt.Axes:
    """
    Plots the cumulative probability distribution of a given NumPy array of numbers,
    representing how the cumulative probability increases with the sorted data indexes.

    Parameters:
    - data (numpy.ndarray): The input NumPy array of non-negative numbers.

    Returns:
    - matplotlib.pyplot.Axes: The plot of cumulative probabilities.

    Requirements:
    - numpy
    - matplotlib

    Raises:
    - ValueError: If the input array contains negative numbers or NaNs.
    - TypeError: If the input array contains non-numeric inputs.

    Note:
    - In case of an all-zeros input, the cumulative probability remains at 0 across all indexes.
    - The plot uses marker ('o') and a solid line ('-') for the cumulative probability curve.
    - The plot is titled "Cumulative Probability Plot", with "Index" on the x-axis and
      "Cumulative Probability" on the y-axis.

    Example:
    >>> ax = task_func(np.array([1, 2, 3, 4, 5]))
    >>> ax.get_title()
    'Cumulative Probability Plot'
    """
    if not isinstance(data, np.ndarray):
        raise TypeError("The input data must be a NumPy array.")
    if not np.issubdtype(data.dtype, np.number):
        raise TypeError("The input data must be a NumPy array of numbers.")
    if np.any(data < 0):
        raise ValueError("The input data must be a NumPy array of non-negative numbers.")
    if np.any(np.isnan(data)):
        raise ValueError("The input data must be a NumPy array of numbers.")

    data = np.sort(data)
    cumulative_prob = np.cumsum(data) / np.sum(data)

    fig, ax = plt.subplots()
    ax.plot(data, cumulative_prob, marker='o', linestyle='-')
    ax.set_title("Cumulative Probability Plot")
    ax.set_xlabel("Index")
    ax.set_ylabel("Cumulative Probability")
    return ax