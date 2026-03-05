
import pandas as pd
import matplotlib.pyplot as plt
# Constants for pie chart colors
COLORS = ['r', 'g', 'b', 'y', 'm']
def task_func(df, col, title=None):
    # Check if input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a DataFrame")
    # Check if DataFrame is not empty
    if df.empty:
        raise ValueError("DataFrame must not be empty")
    # Check if column exists in DataFrame
    if col not in df.columns:
        raise ValueError("Column '{}' does not exist in DataFrame".format(col))
    # Get unique values in column
    unique_vals = df[col].unique()
    # Create pie chart
    fig, ax = plt.subplots()
    ax.pie(unique_vals, colors=COLORS, autopct='%1.1f%%')
    # Set title if specified
    if title:
        ax.set_title(title)
    # Return axes object
    return ax