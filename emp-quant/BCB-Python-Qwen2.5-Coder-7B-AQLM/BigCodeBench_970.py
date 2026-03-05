
import numpy as np
import matplotlib.pyplot as plt

def task_func(data: np.ndarray) -> plt.Axes:
    # Check for negative numbers or NaNs
    if np.any(data < 0) or np.isnan(data).any():
        raise ValueError("Input array contains negative numbers or NaNs.")
    
    # Check for non-numeric inputs
    if not np.issubdtype(data.dtype, np.number):
        raise TypeError("Input array contains non-numeric inputs.")
    
    # Sort the data
    sorted_data = np.sort(data)
    
    # Calculate cumulative probability
    cumulative_probability = np.arange(1, len(sorted_data) + 1) / len(sorted_data)
    
    # Plot the cumulative probability distribution
    fig, ax = plt.subplots()
    ax.plot(sorted_data, cumulative_probability, marker='o', linestyle='-', color='b')
    ax.set_title("Cumulative Probability Plot")
    ax.set_xlabel("Index")
    ax.set_ylabel("Cumulative Probability")
    
    return ax