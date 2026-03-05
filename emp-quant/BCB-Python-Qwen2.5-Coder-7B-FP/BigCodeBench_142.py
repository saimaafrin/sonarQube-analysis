import numpy as np
import matplotlib.pyplot as plt
def task_func():
    """
    Generate diagrams for the sine and cosine functions over the interval [0, 2π].

    Returns:
        Figure: A Matplotlib Figure object containing the plots.
        ndarray: An array of Matplotlib Axes objects for the subplots.
    """
    # Generate x values from 0 to 2π
    x = np.linspace(0, 2 * np.pi, 100)

    # Calculate sine and cosine values
    sine_values = np.sin(x)
    cosine_values = np.cos(x)

    # Create a figure and a set of subplots
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))

    # Plot the sine function
    axes[0].plot(x, sine_values, label='Sine function')
    axes[0].set_xlabel('x')
    axes[0].set_ylabel('sin(x)')
    axes[0].set_title('Sine function')
    axes[0].legend()

    # Plot the cosine function
    axes[1].plot(x, cosine_values, label='Cosine function')
    axes[1].set_xlabel('x')
    axes[1].set_ylabel('cos(x)')
    axes[1].set_title('Cosine function')
    axes[1].legend()

    # Return the figure and axes
    return fig, axes