import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def task_func(rows=5, cols=5):
    """
    Generates a DataFrame with random numerical data and visualizes this data in a stacked bar chart for specified categories.
    The function should raise the exception for: ValueError: If the number of columns exceeds the number of available categories.
    The function should output with:
        matplotlib.axes._axes.Axes: The Axes object displaying the stacked bar chart.
    """
    # Generate random data
    data = np.random.randint(1, 100, size=(rows, cols))
    df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D', 'E'])

    # Check if the number of columns exceeds the number of available categories
    if cols > len(df.columns):
        raise ValueError("The number of columns exceeds the number of available categories.")

    # Create a stacked bar chart
    ax = df.plot(kind='bar', stacked=True, figsize=(10, 6))

    # Set the title and labels
    ax.set_title("Stacked Bar Chart")
    ax.set_xlabel("Categories")
    ax.set_ylabel("Values")

    # Return the Axes object
    return ax
rows = 5
cols = 5