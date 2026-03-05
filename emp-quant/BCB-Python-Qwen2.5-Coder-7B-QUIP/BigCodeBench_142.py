
import numpy as np
import matplotlib.pyplot as plt

def task_func():
    # Generate data for sine and cosine functions
    x = np.linspace(0, 2 * np.pi, 100)
    y_sine = np.sin(x)
    y_cosine = np.cos(x)

    # Create a figure and a set of subplots
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))

    # Plot the sine function
    axs[0].plot(x, y_sine, label='Sine function')
    axs[0].set_title('Sine function')
    axs[0].set_xlabel('x')
    axs[0].set_ylabel('sin(x)')
    axs[0].legend()

    # Plot the cosine function
    axs[1].plot(x, y_cosine, label='Cosine function')
    axs[1].set_title('Cosine function')
    axs[1].set_xlabel('x')
    axs[1].set_ylabel('cos(x)')
    axs[1].legend()

    # Return the figure and axes
    return fig, axs