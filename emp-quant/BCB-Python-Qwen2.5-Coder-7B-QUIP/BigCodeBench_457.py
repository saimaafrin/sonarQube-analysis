
import pandas as pd
import numpy as np
def task_func(L):
    # Check if the input is a list of lists of integers
    if not isinstance(L, list) or not all(isinstance(sublist, list) for sublist in L) or not all(isinstance(item, int) for sublist in L for item in sublist):
        raise TypeError("Input must be a list of lists of integers")
    
    # Flatten the list and ignore empty sublists
    flattened = [item for sublist in L if sublist and all(sublist)]
    
    # Check if the flattened list is not empty
    if not flattened:
        raise ValueError("Input list cannot be empty")
    
    # Create a DataFrame from the flattened list
    df = pd.DataFrame(flattened, columns=['value'])
    
    # Plot the histogram
    ax = df['value'].plot(kind='hist', bins='auto', rwidth=0.8, legend=False)
    
    return ax