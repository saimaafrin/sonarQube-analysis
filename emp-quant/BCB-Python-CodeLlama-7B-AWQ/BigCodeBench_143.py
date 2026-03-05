import numpy as np
import matplotlib.pyplot as plt
def task_func():
    # Define the equation
    y = 2 * x + 1

    # Define the x-axis range
    x_range = np.linspace(-10, 10, 100)

    # Define the y-axis range
    y_range = np.linspace(0, 10, 100)

    # Create the plot
    fig, ax = plt.subplots()
    ax.plot(x_range, y_range, label='y=2x+1')
    ax.scatter(2, 5, marker='o', color='green', label='Solution')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Solution of the equation y=2x+1 at x=2')
    ax.legend()

    return ax