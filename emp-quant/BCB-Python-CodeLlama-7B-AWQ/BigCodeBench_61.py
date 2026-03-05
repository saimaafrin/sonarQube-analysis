import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
PLOT_TITLE = 'Square root plot'
X_LABEL = 'x'
Y_LABEL = 'sqrt(x)'
TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
def task_func(result):
    # Extract the square root values from the input list of dictionaries
    square_root_values = [d['from_user'] for d in result]

    # Round each square root value to 2 decimals
    square_root_values = [round(x, 2) for x in square_root_values]

    # Create a plot of the square root values
    fig, ax = plt.subplots()
    ax.plot(square_root_values)
    ax.set_title(PLOT_TITLE)
    ax.set_xlabel(X_LABEL)
    ax.set_ylabel(Y_LABEL)
    ax.set_xlim([0, 10])
    ax.set_ylim([0, 10])
    ax.grid(True)

    # Annotate the graph with the current date and time
    now = datetime.now()
    ax.text(0.5, 0.95, f'{now.strftime(TIME_FORMAT)}', ha='center')

    # Return the plot and the list of square root values
    return ax, square_root_values
result = [{'from_user': 1}, {'from_user': 4}, {'from_user': 9}]