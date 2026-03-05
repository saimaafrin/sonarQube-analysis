import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def task_func(a, b):
    """
    Generates a pandas DataFrame with random values based on lists 'a' and 'b', and plots it as a bar chart.
    
    Parameters:
    a (list): List of row indices for the DataFrame.
    b (list): List of values to be used for generating the DataFrame columns.
    
    Returns:
    matplotlib.axes.Axes: The Axes object of the plotted bar chart.
    """
    # Create a DataFrame with random values
    df = pd.DataFrame(np.random.rand(len(a), len(b)), index=a, columns=b)
    
    # Plot the DataFrame as a bar chart
    ax = df.plot(kind='bar', figsize=(10, 6))
    
    # Set the title and labels
    ax.set_title('Random Values Bar Chart')
    ax.set_xlabel('Row Indices')
    ax.set_ylabel('Random Values')
    
    # Show the plot
    plt.show()
    
    return ax