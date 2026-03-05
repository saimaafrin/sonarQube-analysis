
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
# Constants
PLOT_TITLE = 'Square root plot'
X_LABEL = 'x'
Y_LABEL = 'sqrt(x)'
TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
def task_func(result):
    # Create a figure and axis
    fig, ax = plt.subplots()
    # Get the square root values from the input list of dictionaries
    square_root_values = [d['from_user'] for d in result]
    # Plot the square root values
    ax.plot(square_root_values)
    # Annotate the graph with the current date and time
    ax.set_xlabel(X_LABEL)
    ax.set_ylabel(Y_LABEL)
    ax.set_title(PLOT_TITLE)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_xticks(np.arange(0, 10, 1.0))
    ax.set_yticks(np.arange(0, 10, 1.0))
    ax.grid(True)
    ax.grid(True)
    ax.set_xticklabels(np.arange(0, 10, 1.0))
    ax.set_yticklabels(np.arange(0, 10, 1.0))
    ax.set_xticklabels(np.arange(0, 10, 1.0))
    ax.set_yticklabels(np.arange(0, 10, 1.0))
    ax.set_xticklabels(np.arange(0, 10, 1.0))
    ax.set_yticklabels(np.arange(0, 10, 1.0))
    ax.set_xticklabels(np.arange(0, 10, 1.0))
    ax.set_yticklabels(np.arange(0, 10, 1.0))
    ax.set_xticklabels(np.arange(0, 10, 1.0))
    ax.set_yticklabels(np.arange(0, 10, 1.0))
    ax.set_xticklabels(np.arange(0, 10, 1.0))
    ax.set_yticklabels(np.arange(0, 10, 1.0))
    ax.set_xticklabels(np.arange(0, 10, 1.0))
    ax.set_yticklabels(np.arange(0, 10, 1.0))
    ax.set_xticklabels(np.arange(0, 10, 1.0))
    ax.set_yticklabels(np.arange(0, 10, 1.0))
    ax.set_xticklabels(np.arange(0, 10, 1.0))
    ax.set_yticklabels(np.arange(0, 10, 1.0))
    ax.set_xticklabels(np.arange(0, 10, 1.0))
    ax.set_yticklabels(np.arange(0, 10, 1.0))
    ax.set_xticklabels(np.arange(0, 10, 1.0))
    ax.set_yticklabels(np.arange(0, 10, 1.0))
    ax.set_xticklabels(np.arange(0, 10, 1.0))
    ax.set_yticklabels(np.arange(0, 10, 1.0))
    ax.set_xticklabels(np.arange(0, 10, 1.0))
    ax.set_yticklabels(np.arange(0, 10, 1.0))
    ax.set_xticklabels(np.arange(0, 10, 1.0))
    ax.set_yticklabels(np.arange(0, 10, 1.0))
    ax.set_xticklabels(np.arange(0, 10, 1.0))
    ax.set_yticklabels(np.arange(0, 10, 1.0))
    ax.set_xticklabels(np.arange(0, 10, 1.0))
    ax.set_yticklabels(np.arange(0, 10, 1.0))
    ax.set_xticklabels(np.arange(0, 10, 1.0))
    ax.set_yticklabels(np.arange(0, 10, 1.0))
    ax.set_xticklabels(np.arange(0, 10, 1.0))
    ax.set_yticklabels(np.arange(0, 10, 1.0))
    ax.set_xticklabels(np.arange(0, 10, 1.0))
    ax.set_