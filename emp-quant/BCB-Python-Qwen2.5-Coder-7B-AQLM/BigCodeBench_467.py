
import matplotlib.pyplot as plt
import numpy as np

def task_func(n, seed=0):
    # Set the seed for reproducibility
    np.random.seed(seed)
    
    # Generate 'n' random points
    points = np.random.rand(n, 2)
    
    # Create a figure and axis
    fig, ax = plt.subplots()
    
    # Plot the points
    ax.scatter(points[:, 0], points[:, 1])
    
    # Set the title and labels
    ax.set_title("Scatter plot of random points")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    
    # Return the figure and the list of points
    return fig, points.tolist()