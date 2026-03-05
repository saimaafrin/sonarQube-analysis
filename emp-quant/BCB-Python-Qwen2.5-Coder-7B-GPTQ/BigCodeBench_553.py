import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
COLUMNS = ['A', 'B', 'C', 'D', 'E']
def task_func(a, b):
    """
    Generates a pandas DataFrame with random values based on lists 'a' and 'b', and plots it as a bar chart.
    
    Parameters:
    a (list): List of strings to be used as row indices.
    b (list): List of integers to determine the number of columns.
    
    Returns:
    matplotlib.axes.Axes: The Axes object of the plotted bar chart.
    """
    # Create a DataFrame with random values
    data = {col: np.random.rand(len(a)) for col in COLUMNS[:len(b)]}
    df = pd.DataFrame(data, index=a)
    
    # Plot the DataFrame as a bar chart
    ax = df.plot(kind='bar', figsize=(10, 6))
    plt.title('Bar Chart of Random Values')
    plt.xlabel('Row Index')
    plt.ylabel('Random Value')
    plt.show()
    
    return ax
a = ['row1', 'row2', 'row3']
b = [3, 2, 4]