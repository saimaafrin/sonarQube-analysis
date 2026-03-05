
import numpy as np
import matplotlib.pyplot as plt

def task_func():
    # Generate x values from -10 to 10
    x = np.linspace(-10, 10, 100)
    # Calculate y values using the equation y = 2x + 1
    y = 2 * x + 1
    
    # Create a figure and a set of subplots
    fig, ax = plt.subplots()
    
    # Plot the line y = 2x + 1
    ax.plot(x, y, label='y=2x+1', color='red')
    
    # Mark the solution at x = 2, y = 5 with a green circle marker
    ax.plot(2, 5, 'o', color='green', label='x=2, y=5')
    
    # Set the title and labels
    ax.set_title('Solution of the equation y=2x+1 at x=2')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    
    # Set the x-axis range
    ax.set_xlim(-10, 10)
    
    # Set the y-axis range based on the equation
    ax.set_ylim(-10, 10)
    
    # Add a legend
    ax.legend()
    
    # Return the figure and axes object
    return ax