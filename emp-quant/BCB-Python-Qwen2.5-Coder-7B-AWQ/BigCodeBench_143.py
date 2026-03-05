import numpy as np
import matplotlib.pyplot as plt
def task_func():
    # Generate x values from -10 to 10
    x = np.linspace(-10, 10, 400)
    # Calculate y values using the equation y = 2x + 1
    y = 2 * x + 1
    
    # Create a figure and axis object
    fig, ax = plt.subplots()
    
    # Plot the line y = 2x + 1
    ax.plot(x, y, label='y=2x+1', color='red')
    
    # Mark the solution at x = 2, y = 5 with a green circle marker
    ax.plot(2, 5, 'go', label='Solution at x=2')
    
    # Set the title of the plot
    ax.set_title('Solution of the equation y=2x+1 at x=2')
    
    # Set the labels for the x and y axes
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    
    # Adjust the y-axis limits based on the equation
    ax.set_ylim(-10, 21)
    
    # Add a legend to the plot
    ax.legend()
    
    # Return the axis object
    return ax