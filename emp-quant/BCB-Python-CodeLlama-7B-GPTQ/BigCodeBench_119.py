import numpy as np
import matplotlib.pyplot as plt
def task_func():
    # Create a figure and axis object
    fig, ax = plt.subplots()

    # Define the x and y values for the parabola
    x = np.linspace(-10, 10, 400)
    y = x**2

    # Plot the parabola
    ax.plot(x, y)

    # Set the title, labels, and grid
    ax.set_title('y = x^2')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(True)

    # Show the plot
    plt.show()