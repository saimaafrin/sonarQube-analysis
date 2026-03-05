import matplotlib.pyplot as plt
import numpy as np
def task_func(ax, radius):
    """
    Draw a circle with a given radius on the polar chart 'ax' and set radial ticks.
    This function manipulates plot data using matplotlib.
    Note that:
        - If the radius is negative this function will raise ValueError.
        - If 'ax' is not a polar plot this function will raise TypeError.
    The function should output with:
        matplotlib.axes._axes.Axes: The modified Axes object with the circle plotted.
    """
    if not isinstance(ax, plt.PolarAxes):
        raise TypeError("'ax' must be a polar plot")
    if radius < 0:
        raise ValueError("radius must be non-negative")

    # Set the radial ticks
    ax.set_rmax(radius)
    ax.set_rticks(np.linspace(0, radius, 4))
    ax.set_rlabel_position(90)

    # Draw the circle
    ax.plot(np.linspace(0, 2 * np.pi, 100), np.zeros_like(np.linspace(0, 2 * np.pi, 100)), 'bo-', lw=2)

    return ax