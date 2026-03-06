
import heapq
import math
import matplotlib.pyplot as plt

def task_func(l1, l2, N=10):
    # Ensure both lists have the same length
    if len(l1) != len(l2):
        raise ValueError("Both lists must have the same length")
    
    # Calculate the absolute differences
    differences = [abs(a - b) for a, b in zip(l1, l2)]
    
    # Find the N largest differences
    largest_differences = heapq.nlargest(N, differences)
    
    # Square the differences
    squared_differences = [d**2 for d in largest_differences]
    
    # Take the square root of the squared differences
    sqrt_differences = [math.sqrt(d) for d in squared_differences]
    
    # Create a plot
    fig, ax = plt.subplots()
    ax.plot(sqrt_differences, marker='o')
    ax.set_xlabel('Index')
    ax.set_ylabel('Square Root of Squared Differences')
    ax.set_title(f'Top {N} Largest Differences')
    
    return ax