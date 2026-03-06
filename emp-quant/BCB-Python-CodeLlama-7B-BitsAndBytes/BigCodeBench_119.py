
import numpy as np
import matplotlib.pyplot as plt

def task_func():
    # Generate x and y values for the parabola
    x = np.linspace(-10, 10, 400)
    y = x**2

    # Create the plot
    plt.plot(x, y)

    # Set the title, labels, and grid
    plt.title('y = x^2')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)

    # Show the plot
    plt.show()

task_func()