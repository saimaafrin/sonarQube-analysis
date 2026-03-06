
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Constants
PLOT_TITLE = 'Square root plot'
X_LABEL = 'x'
Y_LABEL = 'sqrt(x)'
TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

def task_func(result):
    # Extract the square root values from the input list of dictionaries
    x_values = [d['from_user'] for d in result]

    # Calculate the square root values
    y_values = [np.sqrt(x) for x in x_values]

    # Round the square root values to 2 decimals
    y_values = [round(y, 2) for y in y_values]

    # Create the plot
    fig, ax = plt.subplots()
    ax.plot(x_values, y_values)
    ax.set_title(PLOT_TITLE)
    ax.set_xlabel(X_LABEL)
    ax.set_ylabel(Y_LABEL)
    ax.set_xlim([min(x_values), max(x_values)])
    ax.set_ylim([min(y_values), max(y_values)])
    ax.grid()

    # Annotate the plot with the current date and time
    now = datetime.now()
    ax.text(0.5, 0.95, f'{now.strftime(TIME_FORMAT)}', ha='center', va='center', fontsize=14)

    return y_values, ax