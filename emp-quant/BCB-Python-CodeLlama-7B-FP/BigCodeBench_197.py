import heapq
import math
import matplotlib.pyplot as plt
def task_func(l1, l2, N=10):
    """
    Find the N biggest differences between the respective elements of the list 'l1' and list 'l2', square the differences, take the square root and return the plotted values as a matplotlib Axes object.
    """
    # Calculate the differences between the elements of l1 and l2
    diffs = [abs(l1[i] - l2[i]) for i in range(len(l1))]
    
    # Sort the differences in descending order
    diffs = sorted(diffs, reverse=True)
    
    # Take the top N differences
    diffs = diffs[:N]
    
    # Square the differences
    diffs = [d**2 for d in diffs]
    
    # Take the square root of the squared differences
    diffs = [math.sqrt(d) for d in diffs]
    
    # Plot the differences
    fig, ax = plt.subplots()
    ax.plot(diffs)
    ax.set_xlabel('Index')
    ax.set_ylabel('Difference')
    ax.set_title('Differences between l1 and l2')
    return ax
l1 = [1, 2, 3, 4, 5]
l2 = [2, 3, 4, 5, 6]
N = 3