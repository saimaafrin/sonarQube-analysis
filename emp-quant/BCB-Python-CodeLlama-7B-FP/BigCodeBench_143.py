import numpy as np
import matplotlib.pyplot as plt
def task_func():
    # Define the equation
    y = 2 * x + 1

    # Define the range of x values
    x_range = np.linspace(-10, 10, 100)

    # Plot the equation
    plt.plot(x_range, y, label='y=2x+1')

    # Mark the solution point
    plt.scatter(2, 5, c='g', marker='o', label='Solution')

    # Add a title, x-axis label, and y-axis label
    plt.title('Solution of the equation y=2x+1 at x=2')
    plt.xlabel('x')
    plt.ylabel('y')

    # Add a legend
    plt.legend()

    # Show the plot
    plt.show()