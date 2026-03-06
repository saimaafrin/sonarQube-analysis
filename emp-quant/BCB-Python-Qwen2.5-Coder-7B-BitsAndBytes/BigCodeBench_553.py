
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Constants
COLUMNS = ['A', 'B', 'C', 'D', 'E']

def task_func(a, b):
    """
    Generates a pandas DataFrame with random values based on lists 'a' and 'b',
    and plots it as a bar chart.

    Parameters:
    a (list): A list of strings used as the row indices for the DataFrame.
    b (list): A list of integers determining the number of columns in the DataFrame.

    Returns:
    matplotlib.axes.Axes: The Axes object of the plotted bar chart.
    """
    # Create a DataFrame with random values
    df = pd.DataFrame(np.random.rand(len(a), len(b)), index=a, columns=COLUMNS[:len(b)])
    
    # Plot the DataFrame as a bar chart
    ax = df.plot(kind='bar')
    
    return ax