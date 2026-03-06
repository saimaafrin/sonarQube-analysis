
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Constants
PLOT_TITLE = 'Square root plot'
X_LABEL = 'x'
Y_LABEL = 'sqrt(x)'
TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

def task_func(result):
    # Extract values associated with the key 'from_user'
    x_values = [item['from_user'] for item in result]
    
    # Calculate square root values and round them to 2 decimal places
    sqrt_values = np.round(np.sqrt(x_values), 2)
    
    # Create a figure and axis for plotting
    fig, ax = plt.subplots()
    
    # Plot the square root values
    ax.plot(x_values, sqrt_values, marker='o')
    
    # Set the title and labels
    ax.set_title(PLOT_TITLE)
    ax.set_xlabel(X_LABEL)
    ax.set_ylabel(Y_LABEL)
    
    # Annotate the plot with the current date and time
    current_time = datetime.now().strftime(TIME_FORMAT)
    ax.annotate(current_time, xy=(0.5, 0.5), xytext=(0.5, 0.6),
                 textcoords='axes fraction', ha='center', va='center',
                 bbox=dict(boxstyle="round,pad=0.5", fc="yellow", ec="k"))
    
    # Show the plot
    plt.show()
    
    return np.array(sqrt_values), ax