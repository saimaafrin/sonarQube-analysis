import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def task_func(column, data):
    """
    Analyzes and visualizes statistical properties of a specified weather data column.
    
    Parameters:
    - column (str): The name of the column to analyze.
    - data (list of dict): A list of weather observations, where each observation is a dictionary.
    
    Returns:
    - result (dict): A dictionary containing the sum, mean, minimum, and maximum values of the specified column,
      and a matplotlib BarContainer object of the histogram plot for the specified column.
    """
    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(data)
    
    # Check if the DataFrame is empty
    if df.empty:
        return {
            'sum': np.nan,
            'mean': np.nan,
            'min': np.inf,
            'max': -np.inf,
            'plot': None
        }
    
    # Calculate the sum, mean, minimum, and maximum values of the specified column
    sum_value = df[column].sum()
    mean_value = df[column].mean()
    min_value = df[column].min()
    max_value = df[column].max()
    
    # Generate a histogram plot of the data in the specified column
    plot = df[column].hist(bins=10, color='blue')
    
    # Return the result as a dictionary
    return {
        'sum': sum_value,
        'mean': mean_value,
        'min': min_value,
        'max': max_value,
        'plot': plot
    }