import numpy as np
import matplotlib.pyplot as plt
def task_func():
    # Generate the x-axis values
    x = np.linspace(0, 2 * np.pi, 100)

    # Generate the sine and cosine functions
    sin_func = np.sin(x)
    cos_func = np.cos(x)

    # Create the figure and subplots
    fig, axs = plt.subplots(2, 1, figsize=(10, 6))

    # Plot the sine function
    axs[0].plot(x, sin_func)
    axs[0].set_title('Sine function')
    axs[0].set_xlabel('x')
    axs[0].set_ylabel('sin(x)')

    # Plot the cosine function
    axs[1].plot(x, cos_func)
    axs[1].set_title('Cosine function')
    axs[1].set_xlabel('x')
    axs[1].set_ylabel('cos(x)')

    # Return the figure and subplots
    return fig, axs