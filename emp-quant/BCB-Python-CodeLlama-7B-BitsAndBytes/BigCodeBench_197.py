
import heapq
import math
import matplotlib.pyplot as plt

def task_func(l1, l2, N=10):
    # Find the N biggest differences between the respective elements of the lists
    diffs = [abs(l1[i] - l2[i]) for i in range(len(l1))]
    top_diffs = heapq.nlargest(N, diffs)

    # Square the differences and take the square root
    squared_diffs = [x**2 for x in top_diffs]
    roots = [math.sqrt(x) for x in squared_diffs]

    # Plot the differences
    fig, ax = plt.subplots()
    ax.plot(roots)
    ax.set_xlabel('Index')
    ax.set_ylabel('Difference')
    ax.set_title('N Biggest Differences')
    return ax