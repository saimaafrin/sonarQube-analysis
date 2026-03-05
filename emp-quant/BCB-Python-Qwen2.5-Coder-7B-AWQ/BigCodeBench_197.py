import heapq
import math
import matplotlib.pyplot as plt
def task_func(l1, l2, N=10):
    # Calculate the absolute differences between corresponding elements
    differences = [abs(a - b) for a, b in zip(l1, l2)]
    
    # Find the N largest differences
    largest_diffs = heapq.nlargest(N, differences)
    
    # Square the differences
    squared_diffs = [math.sqrt(diff) for diff in largest_diffs]
    
    # Create a matplotlib figure and axis
    fig, ax = plt.subplots()
    
    # Plot the squared differences
    ax.plot(squared_diffs)
    
    # Return the matplotlib Axes object
    return ax