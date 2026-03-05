import pandas as pd
import matplotlib.pyplot as plt
COLORS = ['r', 'g', 'b', 'y', 'm']
def task_func(df, col, title=None):
    """
    Draw a pie chart of the number of unique values in a given DataFrame column with an optional title.
    Note that:
    Each unique value in the column is represented by a slice in the pie chart with a unique color from a predefined set.
    The pie chart can have a title if specified.
    The function should raise the exception for:
    The input df must be DataFrame, not be empty, and must contain the specified column, if it is not, the function will raise ValueError.
    The function should output with:
        Axes: A matplotlib axes object representing the pie chart.
    """
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("The input must be a DataFrame")
    # Check if the DataFrame is not empty
    if df.empty:
        raise ValueError("The DataFrame must not be empty")
    # Check if the specified column exists in the DataFrame
    if col not in df.columns:
        raise ValueError("The column does not exist in the DataFrame")
    # Get the unique values in the specified column
    unique_values = df[col].unique()
    # Get the number of unique values
    num_unique_values = len(unique_values)
    # Create a pie chart with the number of unique values
    fig, ax = plt.subplots()
    ax.pie(num_unique_values, colors=COLORS, autopct='%1.1f%%')
    # Set the title of the pie chart
    if title:
        ax.set_title(title)
    # Return the axes object
    return ax
df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10]})