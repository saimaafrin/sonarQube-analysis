
import heapq
import math
import matplotlib.pyplot as plt

def task_func(l1, l2, N=10):
    # Calculate the differences between the elements of l1 and l2
    differences = [abs(l1_i - l2_i) for l1_i, l2_i in zip(l1, l2)]
    
    # Sort the differences in descending order
    sorted_differences = sorted(differences, reverse=True)
    
    # Take the top N differences
    top_N_differences = sorted_differences[:N]
    
    # Square the differences
    squared_differences = [d**2 for d in top_N_differences]
    
    # Take the square root of the squared differences
    root_differences = [math.sqrt(d) for d in squared_differences]
    
    # Plot the root differences
    fig, ax = plt.subplots()
    ax.plot(root_differences)
    ax.set_xlabel('Index')
    ax.set_ylabel('Root Difference')
    ax.set_title('Root Differences')
    return ax