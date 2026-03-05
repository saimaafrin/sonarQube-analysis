import matplotlib.pyplot as plt
import numpy as np
def task_func(ax, radius):
    """
    Draws a circle with a given radius on the polar chart 'ax' and sets radial ticks.
    
    Parameters:
    ax (matplotlib.axes._axes.Axes): The polar plot axes object.
    radius (float): The radius of the circle to be drawn.
    
    Returns:
    matplotlib.axes._axes.Axes: The modified Axes object with the circle plotted.
    
    Raises:
    ValueError: If the radius is negative.
    TypeError: If 'ax' is not a polar plot.
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    
    if not ax.name == 'polar':
        raise TypeError("The provided axes object is not a polar plot.")
    
    # Draw the circle
    theta = np.linspace(0, 2 * np.pi, 100)
    ax.plot(theta, np.full_like(theta, radius), color='blue')
    
    # Set radial ticks
    ax.set_rticks(np.arange(0, radius + 1, 1))
    
    return ax