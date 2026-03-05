import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def task_func(rows=5, cols=5):
    """
    Generates a DataFrame with random numerical data and visualizes this data in a stacked bar chart for specified categories.
    """
    # Generate random data
    data = np.random.rand(rows, cols)
    # Create a DataFrame
    df = pd.DataFrame(data, columns=['Category 1', 'Category 2', 'Category 3'])
    # Check if the number of columns exceeds the number of available categories
    if len(df.columns) > len(df.index):
        raise ValueError("ValueError: The number of columns exceeds the number of available categories.")
    # Create a stacked bar chart
    ax = df.plot(kind='bar', stacked=True, figsize=(10, 6))
    # Set the title and x-axis label
    ax.set_title("Stacked Bar Chart")
    ax.set_xlabel("Categories")
    # Set the y-axis label
    ax.set_ylabel("Values")
    # Return the Axes object
    return ax
rows = 5
cols = 5