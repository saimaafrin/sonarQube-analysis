
import numpy as np
import matplotlib.pyplot as plt
import itertools

def task_func(data_list):
    if not data_list:
        raise ValueError("The data_list is empty.")
    
    # Unzip the list of tuples
    unzipped_data = list(itertools.zip_longest(*data_list, fillvalue=None))
    
    # Filter out None values
    unzipped_data = [list(filter(None, sublist)) for sublist in unzipped_data]
    
    # Convert to numpy arrays for plotting
    unzipped_data = [np.array(sublist) for sublist in unzipped_data]
    
    # Plot the data
    fig, ax = plt.subplots()
    for i, data in enumerate(unzipped_data):
        ax.plot(data, label=f'Position {i+1}')
    
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    ax.set_title('Unzipped Numerical Values')
    ax.legend()
    
    return ax