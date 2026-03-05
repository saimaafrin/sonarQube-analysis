
import numpy as np
import pandas as pd
def task_func(data_str, separator=",", bins=20):
    # Split the input string into a list of values
    data_list = data_str.split(separator)
    
    # Check if the list is empty
    if not data_list:
        raise ValueError("Data is empty")
    
    # Convert the list to a pandas Series of integers
    data_series = pd.Series(data_list, dtype=int)
    
    # Plot the histogram
    fig, ax = plt.subplots()
    ax.hist(data_series, bins=bins, grid=True, rwidth=0.9, color='#607c8e')
    
    # Return the Series and the Axes object
    return data_series, ax