import numpy as np
import matplotlib.pyplot as plt
import itertools
def task_func(data_list):
    if not data_list:
        raise ValueError("The data_list is empty.")
    
    # Unzip the list of tuples
    unzipped_data = list(itertools.zip_longest(*data_list, fillvalue=0))
    
    # Convert the unzipped data to numpy arrays
    arrays = [np.array(values) for values in unzipped_data]
    
    # Plot the numerical values for each position
    for i, array in enumerate(arrays):
        plt.plot(array, label=f'Position {i+1}')
    
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Unzipped Numerical Values')
    plt.legend()
    plt.show()
data_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]