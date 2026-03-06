
import numpy as np
import matplotlib.pyplot as plt
import itertools

def task_func(data_list):
    if not data_list:
        raise ValueError("data_list cannot be empty")
    
    # Unzip the list of tuples
    unzipped_data = list(itertools.zip_longest(*data_list, fillvalue=None))
    
    # Filter out None values
    filtered_data = [list(filter(None, sublist)) for sublist in unzipped_data]
    
    # Plotting
    fig, ax = plt.subplots()
    for i, data in enumerate(filtered_data):
        ax.plot(range(len(data)), data, label=f'Position {i+1}')
    
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    ax.set_title('Plot of Numerical Values from Tuples')
    ax.legend()
    plt.show()
    
    return ax