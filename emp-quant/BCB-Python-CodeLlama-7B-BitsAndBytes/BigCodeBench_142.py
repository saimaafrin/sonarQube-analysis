
import numpy as np
import matplotlib.pyplot as plt

def task_func():
    # Generate the x-values for the plots
    x = np.linspace(0, 2 * np.pi, 100)

    # Plot the sine function
    plt.subplot(121)
    plt.plot(x, np.sin(x))
    plt.title('Sine function')
    plt.xlabel('x')
    plt.ylabel('sin(x)')

    # Plot the cosine function
    plt.subplot(122)
    plt.plot(x, np.cos(x))
    plt.title('Cosine function')
    plt.xlabel('x')
    plt.ylabel('cos(x)')

    # Return the figure and axes objects
    return plt.gcf(), plt.gca()

# Call the function and display the plots
fig, ax = task_func()
fig.show()