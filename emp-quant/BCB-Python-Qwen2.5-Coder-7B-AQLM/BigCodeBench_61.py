
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
    
    # Calculate square root values and round to 2 decimals
    sqrt_values = np.round(np.sqrt(x_values), 2)
    
    # Create a plot
    fig, ax = plt.subplots()
    ax.plot(x_values, sqrt_values, marker='o')
    
    # Annotate the plot with the current date and time
    current_time = datetime.now().strftime(TIME_FORMAT)
    ax.annotate(current_time, (0.5, 0.5), xycoords='axes fraction', fontsize=12)
    
    # Set plot title and labels
    ax.set_title(PLOT_TITLE)
    ax.set_xlabel(X_LABEL)
    ax.set_ylabel(Y_LABEL)
    
    # Return the list of square values and the plot
    return sqrt_values, ax