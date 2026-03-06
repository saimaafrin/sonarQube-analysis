
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler

def task_func(x, y, labels):
    """
    Scales the 'x' and 'y' arrays using the standard scaler of sklearn and plots them with given labels.
    
    Parameters:
    - x (list or array-like): The x-coordinates to be scaled.
    - y (list or array-like): The y-coordinates to be scaled.
    - labels (list of str): Labels for each series in the plot.
    
    Returns:
    - matplotlib.figure.Figure: The figure object containing the plot.
    """
    # Ensure inputs are numpy arrays
    x = np.array(x)
    y = np.array(y)
    
    # Initialize the StandardScaler
    scaler_x = StandardScaler()
    scaler_y = StandardScaler()
    
    # Scale the data
    x_scaled = scaler_x.fit_transform(x.reshape(-1, 1)).flatten()
    y_scaled = scaler_y.fit_transform(y.reshape(-1, 1)).flatten()
    
    # Create a new figure
    fig, ax = plt.subplots()
    
    # Plot the scaled data
    for i, label in enumerate(labels):
        ax.plot(x_scaled[i], y_scaled[i], label=label)
    
    # Add legend
    ax.legend()
    
    return fig