import numpy as np
import matplotlib.pyplot as plt
def task_func():
    """
    Draws the linear equation y = 2x + 1 on a 2D plot for x values ranging from -10 to 10, and marks the solution for x = 2 with a green 'o' (circle) marker.
    The plot includes:
    - A red line representing the equation y = 2x + 1, labeled as 'y=2x+1', for x in [-10, 10].
    - A green circle marker indicating the solution at x = 2, y = 5.
    - Title: 'Solution of the equation y=2x+1 at x=2'
    - X-axis labeled as 'x', with a range from -10 to 10.
    - Y-axis labeled as 'y', with a range automatically adjusted based on the equation.
    - A legend indicating labels for the equation and the solution point.
    Returns:
        matplotlib.axes.Axes: An object representing the plot with specified features and ranges.
    """
    # Generate x values
    x = np.linspace(-10, 10, 400)
    # Calculate y values based on the equation y = 2x + 1
    y = 2 * x + 1
    
    # Create the plot
    fig, ax = plt.subplots()
    # Plot the line y = 2x + 1
    ax.plot(x, y, 'r-', label='y=2x+1')
    # Mark the solution at x = 2, y = 5 with a green circle
    ax.plot(2, 5, 'go', label='Solution at x=2')
    
    # Set the title and labels
    ax.set_title('Solution of the equation y=2x+1 at x=2')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    
    # Adjust the y-axis range based on the equation
    ax.set_ylim(-10, 20)
    
    # Add a legend
    ax.legend()
    
    # Return the axes object
    return ax