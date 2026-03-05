
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Constants
PLOT_TITLE = 'Square root plot'
X_LABEL = 'x'
Y_LABEL = 'sqrt(x)'
TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

def task_func(result):
    # Extract square root values from result
    x_values = np.array([d['from_user'] for d in result])
    y_values = np.sqrt(x_values)

    # Round to 2 decimals
    y_values = np.round(y_values, 2)

    # Create plot
    fig, ax = plt.subplots()
    ax.plot(x_values, y_values)
    ax.set_title(PLOT_TITLE)
    ax.set_xlabel(X_LABEL)
    ax.set_ylabel(Y_LABEL)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)

    # Annotate with current date and time
    now = datetime.now()
    ax.text(0.5, 0.95, f'Created at: {now.strftime(TIME_FORMAT)}', ha='center', va='center', transform=ax.transAxes)

    return x_values, ax