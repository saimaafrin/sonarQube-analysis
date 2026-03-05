
import heapq
import math
import matplotlib.pyplot as plt

def task_func(l1, l2, N=10):
    # Calculate the differences between the respective elements of the lists
    differences = [math.sqrt((x - y) ** 2) for x, y in zip(l1, l2)]
    
    # Get the N biggest differences
    biggest_differences = heapq.nlargest(N, differences)
    
    # Create a figure and an axes object
    fig, ax = plt.subplots()
    
    # Plot the differences
    ax.plot(range(len(biggest_differences)), biggest_differences, 'o')
    
    # Return the axes object
    return ax