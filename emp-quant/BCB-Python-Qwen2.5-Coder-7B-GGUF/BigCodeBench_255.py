
import matplotlib.pyplot as plt
import numpy as np
# Constants
FUNCTIONS = [np.sin, np.cos, np.tan]

def task_func(ax, func_index):
    if not isinstance(ax, plt.Axes):
        raise ValueError("The input ax must be a matplotlib.axes._axes.Axes object.")
    
    theta = np.linspace(0, 2 * np.pi, 100)
    r = FUNCTIONS[func_index](theta)
    
    ax.plot(theta, r, label=f'{FUNCTIONS[func_index].__name__}')
    ax.set_rticks(np.arange(0, 1.1, 0.25) * 45)  # Set radial ticks at 45-degree intervals
    ax.set_rlabel_position(0)  # Move radial labels to the top
    ax.legend()
    
    return ax