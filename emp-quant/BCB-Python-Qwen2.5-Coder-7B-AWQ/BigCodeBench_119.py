import numpy as np
import matplotlib.pyplot as plt
def task_func():
    """
    Plots a parabola y = x^2 using matplotlib.
    """
    # Generate x values from -10 to 10 with 400 points
    x = np.linspace(-10, 10, 400)
    # Calculate y values based on the equation y = x^2
    y = x**2
    
    # Create a plot
    plt.figure()
    plt.plot(x, y, label='y = x^2')
    plt.title('y = x^2')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()
    plt.show()