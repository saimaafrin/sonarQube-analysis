
import matplotlib.pyplot as plt
import numpy as np

def task_func(n, seed=0):
    # Set the seed for the random number generator
    np.random.seed(seed)
    
    # Generate 'n' random points
    x = np.random.rand(n)
    y = np.random.rand(n)
    
    # Create a scatter plot
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    
    # Set the title and labels
    ax.set_title('Scatter plot of random points')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    
    # Return the plot and the list of points
    return fig, list(zip(x, y))