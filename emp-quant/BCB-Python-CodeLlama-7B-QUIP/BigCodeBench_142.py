
import numpy as np
import matplotlib.pyplot as plt

def task_func():
    # Define the x-axis values for the sine and cosine functions
    x = np.linspace(0, 2 * np.pi, 100)

    # Plot the sine function
    plt.subplot(2, 1, 1)
    plt.plot(x, np.sin(x))
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    plt.title('Sine function')

    # Plot the cosine function
    plt.subplot(2, 1, 2)
    plt.plot(x, np.cos(x))
    plt.xlabel('x')
    plt.ylabel('cos(x)')
    plt.title('Cosine function')

    # Return the figure object
    return plt.gcf()

# Call the function and display the plots
fig = task_func()
plt.show()