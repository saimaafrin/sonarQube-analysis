
import heapq
import math
import matplotlib.pyplot as plt

def task_func(l1, l2, N=10):
    # Calculate the differences between elements of l1 and l2
    differences = [abs(x - y) for x, y in zip(l1, l2)]
    
    # Find the N biggest differences
    biggest_differences = heapq.nlargest(N, differences)
    
    # Square the differences
    squared_differences = [math.sqrt(diff) for diff in biggest_differences]
    
    # Create a range for the x-axis
    x = range(1, N + 1)
    
    # Plot the squared differences
    fig, ax = plt.subplots()
    ax.plot(x, squared_differences, marker='o')
    ax.set_xlabel('Index')
    ax.set_ylabel('Squared Difference')
    ax.set_title(f'Top {N} Biggest Differences Squared')
    
    return ax