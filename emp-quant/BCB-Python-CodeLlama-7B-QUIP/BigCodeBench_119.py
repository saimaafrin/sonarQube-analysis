
import numpy as np
import matplotlib.pyplot as plt

def task_func():
    # Create a range of x values from -10 to 10 with 400 points
    x_values = np.linspace(-10, 10, 400)

    # Define the parabola function
    y_values = x_values ** 2

    # Plot the parabola
    plt.plot(x_values, y_values)

    # Set the title, labels, and grid
    plt.title("y = x^2")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)

    # Show the plot
    plt.show()

# Call the function
task_func()