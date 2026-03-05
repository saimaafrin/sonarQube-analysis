
import heapq
import math
import matplotlib.pyplot as plt

def task_func(l1, l2, N=10):
    # Calculate the differences between the elements of the lists
    diffs = [abs(l1[i] - l2[i]) for i in range(N)]

    # Square the differences
    squared_diffs = [diff ** 2 for diff in diffs]

    # Take the square root of the squared differences
    root_squared_diffs = [math.sqrt(diff) for diff in squared_diffs]

    # Plot the squared differences
    fig, ax = plt.subplots()
    ax.plot(root_squared_diffs)
    ax.set_xlabel("Index")
    ax.set_ylabel("Squared Difference")
    ax.set_title("Squared Differences between Lists")
    return ax