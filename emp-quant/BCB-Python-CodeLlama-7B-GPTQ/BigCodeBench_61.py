import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
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
    ax.plot(x_values, y_values, label=PLOT_TITLE)
    ax.set_xlabel(X_LABEL)
    ax.set_ylabel(Y_LABEL)
    ax.set_title(f'Square root plot at {datetime.now().strftime(TIME_FORMAT)}')
    ax.legend()

    # Return the plot and the list of square root values
    return ax, y_values
result = [
    {'from_user': 1},
    {'from_user': 4},
    {'from_user': 9},
    {'from_user': 16},
    {'from_user': 25},
]