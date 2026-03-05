import numpy as np
import matplotlib.pyplot as plt
def task_func():
    # Generate diagrams for the sine and cosine functions over the interval [0, 2π].
    x = np.linspace(0, 2 * np.pi, 100)
    y_sin = np.sin(x)
    y_cos = np.cos(x)

    # Plot the sine and cosine functions.
    fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(8, 6))
    ax[0].plot(x, y_sin, label='Sine function')
    ax[0].set_xlabel('x')
    ax[0].set_ylabel('sin(x)')
    ax[0].legend()
    ax[1].plot(x, y_cos, label='Cosine function')
    ax[1].set_xlabel('x')
    ax[1].set_ylabel('cos(x)')
    ax[1].legend()

    # Return the figure and axes objects.
    return fig, ax