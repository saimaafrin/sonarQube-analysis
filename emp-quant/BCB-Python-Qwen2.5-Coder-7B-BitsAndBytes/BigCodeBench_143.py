
import numpy as np
import matplotlib.pyplot as plt

def task_func():
    # Generate x values from -10 to 10
    x = np.linspace(-10, 10, 400)
    
    # Calculate corresponding y values using the equation y = 2x + 1
    y = 2 * x + 1
    
    # Create a figure and an axes.
    fig, ax = plt.subplots()
    
    # Plot the line y = 2x + 1
    ax.plot(x, y, label='y=2x+1')
    
    # Mark the solution for x = 2 with a green 'o' (circle) marker
    ax.scatter(2, 5, color='green', label='Solution at x=2')
    
    # Set the title of the plot
    ax.set_title('Solution of the equation y=2x+1 at x=2')
    
    # Label the x-axis
    ax.set_xlabel('x')
    
    # Label the y-axis
    ax.set_ylabel('y')
    
    # Adjust the y-axis limits based on the data
    ax.autoscale_view()
    
    # Add a legend
    ax.legend()
    
    return ax