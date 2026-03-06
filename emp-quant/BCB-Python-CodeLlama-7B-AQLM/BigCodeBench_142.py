import numpy as np
import matplotlib.pyplot as plt
def task_func():
    """
    Generate diagrams for the sine and cosine functions over the interval [0, 2π].

    This function plots the sine and cosine functions, setting appropriate titles and axis labels.

    Returns:
        Figure: A Matplotlib Figure object containing the plots.
        ndarray: An array of Matplotlib Axes objects for the subplots, where:
                 - The first Axes object contains the sine function plot.
                 - The second Axes object contains the cosine function plot.

    The sine function plot is labeled 'Sine function', with x-axis labeled 'x' and y-axis labeled 'sin(x)'.
    The cosine function plot is labeled 'Cosine function', with x-axis labeled 'x' and y-axis labeled 'cos(x)'.

    Requirements:
        - numpy
        - matplotlib.pyplot

    Example:
        >>> fig, axs = task_func()
        >>> plt.show()
    """
    # Generate the sine and cosine functions over the interval [0, 2π].
    x = np.linspace(0, 2*np.pi, 100)
    y_sin = np.sin(x)
    y_cos = np.cos(x)

    # Create a figure with two subplots.
    fig, axs = plt.subplots(2, 1, figsize=(10, 10))

    # Plot the sine function.
    axs[0].plot(x, y_sin)
    axs[0].set_title('Sine function')
    axs[0].set_xlabel('x')
    axs[0].set_ylabel('sin(x)')

    # Plot the cosine function.
    axs[1].plot(x, y_cos)
    axs[1].set_title('Cosine function')
    axs[1].set_xlabel('x')
    axs[1].set_ylabel('cos(x)')

    # Return the figure and the subplots.
    return fig, axs