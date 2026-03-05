
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
    # Create a figure and axis
    fig, ax = plt.subplots()
    
    # Initialize the StandardScaler
    scaler = StandardScaler()
    
    # Loop through each pair of x and y arrays and their labels
    for xi, yi, label in zip(x, y, labels):
        # Scale the x and y arrays
        xi_scaled = scaler.fit_transform(xi.reshape(-1, 1)).flatten()
        yi_scaled = scaler.fit_transform(yi.reshape(-1, 1)).flatten()
        
        # Plot the scaled data
        ax.plot(xi_scaled, yi_scaled, label=label)
    
    # Add labels and title
    ax.set_xlabel('Scaled X')
    ax.set_ylabel('Scaled Y')
    ax.set_title('Scaled X and Y Arrays')
    
    # Add legend
    ax.legend()
    
    # Return the figure object
    return fig