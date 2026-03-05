import numpy as np
import matplotlib.pyplot as plt
def task_func(data: np.ndarray) -> plt.Axes:
    """
    Plots the cumulative probability distribution of a given NumPy array of numbers.
    
    Parameters:
    data (np.ndarray): A NumPy array of numbers.
    
    Returns:
    plt.Axes: The plot of cumulative probabilities.
    
    Raises:
    ValueError: If the input array contains negative numbers or NaNs.
    TypeError: If the input array contains non-numeric inputs.
    """
    # Check for negative numbers or NaNs
    if np.any(data < 0) or np.isnan(data).any():
        raise ValueError("Input array contains negative numbers or NaNs.")
    
    # Check for non-numeric inputs
    if not np.issubdtype(data.dtype, np.number):
        raise TypeError("Input array contains non-numeric inputs.")
    
    # Sort the data
    sorted_data = np.sort(data)
    
    # Calculate cumulative probabilities
    cumulative_probabilities = np.arange(1, len(sorted_data) + 1) / len(sorted_data)
    
    # Plot the cumulative probability distribution
    fig, ax = plt.subplots()
    ax.plot(sorted_data, cumulative_probabilities, marker='o', linestyle='-')
    ax.set_title('Cumulative Probability Plot')
    ax.set_xlabel('Index')
    ax.set_ylabel('Cumulative Probability')
    
    return ax
data = np.array([0.1, 0.2, 0.3, 0.4, 0.5])