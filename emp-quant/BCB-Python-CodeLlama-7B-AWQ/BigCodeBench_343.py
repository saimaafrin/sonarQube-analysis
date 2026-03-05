import pandas as pd
import matplotlib.pyplot as plt
COLORS = ['r', 'g', 'b', 'y', 'm']
def task_func(df, col, title=None):
    """
    Draw a pie chart of the number of unique values in a given DataFrame column with an optional title.
    """
    # Check if input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a DataFrame")
    # Check if DataFrame is not empty
    if df.empty:
        raise ValueError("DataFrame is empty")
    # Check if specified column exists in DataFrame
    if col not in df.columns:
        raise ValueError("Column does not exist in DataFrame")
    # Get unique values in column
    unique_values = df[col].unique()
    # Create pie chart
    fig, ax = plt.subplots()
    ax.pie(unique_values, colors=COLORS, autopct='%1.1f%%')
    # Add title if specified
    if title:
        ax.set_title(title)
    # Show pie chart
    plt.show()
    return ax
df = pd.DataFrame({'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})