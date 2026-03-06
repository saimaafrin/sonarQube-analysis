
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def task_func(data_str, separator=",", bins=20):
    # Split the input string by the specified separator
    data_list = data_str.split(separator)
    
    # Check if the list is empty
    if not data_list:
        raise ValueError("Data is empty")
    
    try:
        # Convert the list of strings to integers
        data_series = pd.Series(pd.to_numeric(data_list, downcast='integer'))
        
        # Plot the histogram
        fig, ax = plt.subplots()
        ax.hist(data_series, bins=bins, rwidth=0.9, color='#607c8e')
        ax.grid(True)
        
        return (data_series, ax)
    except ValueError:
        raise ValueError("Failed to convert data to integers")