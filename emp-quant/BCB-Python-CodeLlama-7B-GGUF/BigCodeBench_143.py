
import numpy as np
import matplotlib.pyplot as plt

def task_func():
    # Define the range of x values
    x_range = np.linspace(-10, 10, 100)

    # Define the equation y = 2x + 1
    y_eq = 2 * x_range + 1

    # Create the plot
    fig, ax = plt.subplots()
    ax.plot(x_range, y_eq, label='y=2x+1')

    # Mark the solution point
    ax.scatter(2, 5, c='g', marker='o', label='Solution')

    # Set the title, x-axis label, and y-axis label
    ax.set_title('Solution of the equation y=2x+1 at x=2')
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    # Add a legend
    ax.legend()

    return ax