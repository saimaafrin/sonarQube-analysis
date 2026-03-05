
import pandas as pd
import numpy as np

def task_func(L):
    # Check if the input is a list of lists
    if not isinstance(L, list) or not all(isinstance(sublist, list) for sublist in L):
        raise TypeError("Input must be a list of lists")
    
    # Flatten the list and filter out empty sublists
    flattened_list = [item for sublist in L for item in sublist if item]
    
    # Check if the flattened list contains only integers
    if not all(isinstance(item, int) for item in flattened_list):
        raise TypeError("All elements in the nested list must be integers")
    
    # Create a DataFrame from the flattened list
    df = pd.DataFrame(flattened_list, columns=['Values'])
    
    # Plot the histogram
    ax = df['Values'].hist(bins='auto', rwidth=0.8)
    
    return ax