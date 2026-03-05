import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
PLOT_TITLE = 'Square root plot'
X_LABEL = 'x'
Y_LABEL = 'sqrt(x)'
TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
def task_func(result):
    # Extract values associated with the key 'from_user' from the input list of dictionaries
    x_values = [item['from_user'] for item in result]
    
    # Calculate square root values and round to 2 decimals
    y_values = np.round(np.sqrt(x_values), 2)
    
    # Create a plot
    fig, ax = plt.subplots()
    ax.plot(x_values, y_values, marker='o')
    
    # Annotate the graph with the current date and time
    current_time = datetime.now().strftime(TIME_FORMAT)
    ax.annotate(current_time, (0.05, 0.95), xycoords='axes fraction', fontsize=10, verticalalignment='top')
    
    # Set plot title and labels
    ax.set_title(PLOT_TITLE)
    ax.set_xlabel(X_LABEL)
    ax.set_ylabel(Y_LABEL)
    
    # Return the list of square root values and the plot
    return y_values, ax