import numpy as np
import matplotlib.pyplot as plt
def task_func():
    # Create a range of x values from -10 to 10 with 400 points
    x = np.linspace(-10, 10, 400)

    # Create a range of y values for the parabola
    y = x**2

    # Plot the parabola
    plt.plot(x, y)

    # Set the title, labels, and grid
    plt.title('y = x^2')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)

    # Display the plot
    plt.show()