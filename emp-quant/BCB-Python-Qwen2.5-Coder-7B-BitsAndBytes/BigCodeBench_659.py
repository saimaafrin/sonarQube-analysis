
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

def task_func(x, y, labels):
    """
    Draws normal distributions for multiple pairs of 'x' and 'y' arrays with labels.

    Parameters:
    x (list of array-like): List of x data arrays.
    y (list of array-like): List of y data arrays.
    labels (list of str): List of labels corresponding to each pair of x and y.

    Returns:
    fig (matplotlib.figure.Figure): Matplotlib figure object containing the plots.
    """
    # Create a new figure
    fig, ax = plt.subplots()

    # Plot each normal distribution
    for i in range(len(x)):
        mean_x = np.mean(x[i])
        std_dev_x = np.std(x[i])
        mean_y = np.mean(y[i])
        std_dev_y = np.std(y[i])

        # Draw normal distribution for x
        x_vals = np.linspace(min(x[i]), max(x[i]), 100)
        y_vals_x = stats.norm.pdf(x_vals, mean_x, std_dev_x)
        ax.plot(x_vals, y_vals_x, label=f'{labels[i]} - X Distribution')

        # Draw normal distribution for y
        y_vals = np.linspace(min(y[i]), max(y[i]), 100)
        y_vals_y = stats.norm.pdf(y_vals, mean_y, std_dev_y)
        ax.plot(y_vals, y_vals_y, label=f'{labels[i]} - Y Distribution')

    # Set plot title and labels
    ax.set_title('Normal Distributions for Multiple Chemical Compounds')
    ax.set_xlabel('Values')
    ax.set_ylabel('Probability Density')

    # Add legend
    ax.legend()

    return fig

    # Generate the figure
    fig = task_func(x_data, y_data, labels)

    # Show the plot
    plt.show()