import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def task_func(rows=5, cols=5):
    """
    Generates a DataFrame with random numerical data and visualizes this data in a stacked bar chart for specified categories.
    
    Parameters:
    - rows (int): The number of rows in the DataFrame.
    - cols (int): The number of columns in the DataFrame.
    
    Returns:
    - matplotlib.axes._axes.Axes: The Axes object displaying the stacked bar chart.
    
    Raises:
    - ValueError: If the number of columns exceeds the number of available categories.
    """
    # Define categories
    categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4', 'Category 5']
    
    # Check if the number of columns exceeds the number of available categories
    if cols > len(categories):
        raise ValueError("The number of columns exceeds the number of available categories.")
    
    # Generate random data
    data = np.random.randint(1, 100, size=(rows, cols))
    
    # Create DataFrame
    df = pd.DataFrame(data, columns=categories[:cols])
    
    # Create stacked bar chart
    ax = df.plot(kind='bar', stacked=True)
    
    # Set title and labels
    ax.set_title('Stacked Bar Chart')
    ax.set_xlabel('Index')
    ax.set_ylabel('Values')
    
    return ax