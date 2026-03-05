import numpy as np
import matplotlib.pyplot as plt
import itertools
def task_func(data_list):
    if not data_list:
        raise ValueError("The data_list is empty.")
    
    # Unzip the list of tuples
    unzipped_data = zip(*data_list)
    
    # Convert the unzipped data to numpy arrays for plotting
    x = np.array(list(unzipped_data[0]))
    y = np.array(list(unzipped_data[1]))
    
    # Create a plot
    plt.figure()
    plt.plot(x, y, marker='o')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Plot of Unzipped Numerical Values')
    plt.grid(True)
    
    # Show the plot
    plt.show()
    
    return plt.gca()  # Return the current Axes instance on the current figure
data_list = [(1, 2), (3, 4), (5, 6)]