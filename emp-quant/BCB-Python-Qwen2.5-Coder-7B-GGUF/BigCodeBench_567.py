
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(data):
    # Convert the input string to a pandas Series
    data_series = pd.Series(data.split(','))
    
    # Convert the Series to numeric, coercing errors to NaN
    data_numeric = pd.to_numeric(data_series, errors='coerce')
    
    # Filter out NaN values
    data_filtered = data_numeric.dropna()
    
    # Calculate the bins for the histogram
    bins = np.arange(data_filtered.min(), data_filtered.max() + 2) - 0.5
    
    # Create the histogram
    ax = data_filtered.hist(bins=bins, edgecolor='black')
    
    # Set the labels and title
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram of Values')
    
    # Return the Axes object
    return ax