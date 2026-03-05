import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler
def task_func(x, y, labels):
    """
    Scale the 'x' and 'y' arrays using the standard scaler of sklearn and plot them with given labels.
    Each pair of x and y arrays are scaled independently and plotted as a separate series with a label.
    
    Parameters:
    x (list of np.ndarray): List of x arrays to be scaled.
    y (list of np.ndarray): List of y arrays to be scaled.
    labels (list of str): List of labels for each series.
    
    Returns:
    matplotlib.figure.Figure: The figure object containing the plot.
    """
    # Initialize the figure and axis
    fig, ax = plt.subplots()
    
    # Initialize the StandardScaler
    scaler = StandardScaler()
    
    # Loop through each x and y array with its corresponding label
    for xi, yi, label in zip(x, y, labels):
        # Scale the x and y arrays
        scaled_x = scaler.fit_transform(xi.reshape(-1, 1)).flatten()
        scaled_y = scaler.fit_transform(yi.reshape(-1, 1)).flatten()
        
        # Plot the scaled x and y arrays
        ax.plot(scaled_x, scaled_y, label=label)
    
    # Add a legend to the plot
    ax.legend()
    
    # Return the figure object
    return fig