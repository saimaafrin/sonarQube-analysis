import numpy as np
import matplotlib.pyplot as plt
def task_func():
    # Generate the x-axis values
    x = np.linspace(0, 2 * np.pi, 100)

    # Generate the sine and cosine functions
    sin_func = np.sin(x)
    cos_func = np.cos(x)

    # Create a figure object
    fig = plt.figure(figsize=(8, 6))

    # Create subplots
    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2)

    # Plot the sine and cosine functions
    ax1.plot(x, sin_func, label='Sine function')
    ax2.plot(x, cos_func, label='Cosine function')

    # Set the titles and axis labels
    ax1.set_title('Sine function')
    ax1.set_xlabel('x')
    ax1.set_ylabel('sin(x)')

    ax2.set_title('Cosine function')
    ax2.set_xlabel('x')
    ax2.set_ylabel('cos(x)')

    # Return the figure and axes objects
    return fig, [ax1, ax2]