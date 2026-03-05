
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(data):
    # Convert the input string to a pandas Series
    data = pd.Series(data.split())
    
    # Calculate the range for the histogram bins
    bins = np.arange(data.min(), data.max() + 2) - 0.5
    
    # Create the histogram
    ax = data.plot(kind='hist', bins=bins, edgecolor='k')
    
    # Set the labels and title
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram of Values')
    
    # Return the Axes object
    return ax