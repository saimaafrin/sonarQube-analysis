
import numpy as np
import matplotlib.pyplot as plt
import itertools

def task_func(data_list):
    if not data_list:
        raise ValueError("Data list is empty")
    
    # Unzip the list of tuples
    unzipped = list(zip(*data_list))
    
    # Plot the numerical values
    fig, ax = plt.subplots()
    ax.plot(unzipped[0], unzipped[1], 'o')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Unzipped Numerical Values')
    
    return ax