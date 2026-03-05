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
    diffs.sort(reverse=True)

    # Take the top N differences
    top_diffs = diffs[:N]

    # Square the differences
    squared_diffs = [diff**2 for diff in top_diffs]

    # Take the square root of the squared differences
    root_diffs = [math.sqrt(diff) for diff in squared_diffs]

    # Plot the root differences
    fig, ax = plt.subplots()
    ax.plot(root_diffs)
    ax.set_xlabel('Index')
    ax.set_ylabel('Root Difference')
    ax.set_title('Root Differences')
    return ax
l1 = [1, 2, 3, 4, 5]
l2 = [2, 4, 6, 8, 10]
N = 3