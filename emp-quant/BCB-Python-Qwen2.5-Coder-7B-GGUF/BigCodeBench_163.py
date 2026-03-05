
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def task_func(rows=5, cols=5):
    """
    Generates a DataFrame with random numerical data and visualizes this data in a stacked bar chart for specified categories.
    
    Parameters:
    rows (int): The number of rows in the DataFrame.
    cols (int): The number of columns in the DataFrame.
    
    Returns:
    matplotlib.axes._axes.Axes: The Axes object displaying the stacked bar chart.
    
    Raises:
    ValueError: If the number of columns exceeds the number of available categories.
    """
    if cols > 5:
        raise ValueError("The number of columns exceeds the number of available categories.")
    
    # Generate random data
    data = np.random.rand(rows, cols)
    categories = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']
    df = pd.DataFrame(data, columns=categories[:cols])
    
    # Create a stacked bar chart
    ax = df.plot(kind='bar', stacked=True)
    plt.title('Stacked Bar Chart')
    plt.xlabel('Index')
    plt.ylabel('Values')
    plt.show()
    
    return ax