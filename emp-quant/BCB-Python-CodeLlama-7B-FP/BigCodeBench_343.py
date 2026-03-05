import pandas as pd
import matplotlib.pyplot as plt
COLORS = ['r', 'g', 'b', 'y', 'm']
def task_func(df, col, title=None):
    """
    Draw a pie chart of the number of unique values in a given DataFrame column with an optional title.
    Each unique value in the column is represented by a slice in the pie chart with a unique color from a predefined set.
    The pie chart can have a title if specified.
    The function should raise the exception for:
        - The input df must be DataFrame, not be empty, and must contain the specified column, if it is not, the function will raise ValueError.
    The function should output with:
        - Axes: A matplotlib axes object representing the pie chart.
    """
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a DataFrame")
    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("DataFrame is empty")
    # Check if the specified column exists in the DataFrame
    if col not in df.columns:
        raise ValueError("Column does not exist in DataFrame")
    # Get the unique values in the specified column
    unique_values = df[col].unique()
    # Create a pie chart with the unique values as slices
    fig, ax = plt.subplots()
    ax.pie(unique_values, colors=COLORS)
    # Add a title to the pie chart if specified
    if title:
        ax.set_title(title)
    # Return the axes object
    return ax
df = pd.DataFrame({'A': [1, 2, 3, 4, 5]})