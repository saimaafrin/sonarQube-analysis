import numpy as np
import matplotlib.pyplot as plt
def task_func():
    """
    Plots a parabola y = x^2 using matplotlib.
    """
    # Generate x values from -10 to 10 with 400 points
    x = np.linspace(-10, 10, 400)
    # Calculate y values as x squared
    y = x**2
    
    # Plot the parabola
    plt.plot(x, y)
    # Set the title of the plot
    plt.title('y = x^2')
    # Label the x-axis
    plt.xlabel('x')
    # Label the y-axis
    plt.ylabel('y')
    # Enable the grid
    plt.grid(True)
    # Display the plot
    plt.show()