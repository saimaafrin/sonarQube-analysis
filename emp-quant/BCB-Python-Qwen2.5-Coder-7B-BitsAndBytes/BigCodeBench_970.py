
import numpy as np
import matplotlib.pyplot as plt

def task_func(data: np.ndarray) -> plt.Axes:
    # Check if the input array contains negative numbers or NaNs
    if np.any(data < 0) or np.isnan(np.sum(data)):
        raise ValueError("Input array contains negative numbers or NaNs.")
    
    # Check if the input array contains non-numeric inputs
    if not np.issubdtype(data.dtype, np.number):
        raise TypeError("Input array contains non-numeric inputs.")
    
    # Sort the data
    sorted_data = np.sort(data)
    
    # Calculate the cumulative sum
    cumsum = np.cumsum(sorted_data)
    
    # Normalize the cumulative sum to get cumulative probability
    cumprob = cumsum / cumsum[-1]
    
    # Create the plot
    fig, ax = plt.subplots()
    ax.plot(range(len(cumprob)), cumprob, marker='o', linestyle='-')
    ax.set_title('Cumulative Probability Plot')
    ax.set_xlabel('Index')
    ax.set_ylabel('Cumulative Probability')
    
    return ax