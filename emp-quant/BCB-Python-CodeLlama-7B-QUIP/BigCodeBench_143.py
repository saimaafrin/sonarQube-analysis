
import numpy as np
import matplotlib.pyplot as plt

def task_func():
    # Define the equation y = 2x + 1
    equation = np.array([2, 1])

    # Define the range of x values
    x_range = np.linspace(-10, 10, 100)

    # Define the solution for x = 2
    solution = np.array([2, 5])

    # Plot the equation and the solution
    fig, ax = plt.subplots()
    ax.plot(x_range, equation, label='y=2x+1')
    ax.scatter(solution[0], solution[1], c='g', marker='o', label='x=2')

    # Set the title, x-axis, and y-axis labels
    ax.set_title('Solution of the equation y=2x+1 at x=2')
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    # Set the legend
    ax.legend()

    return ax