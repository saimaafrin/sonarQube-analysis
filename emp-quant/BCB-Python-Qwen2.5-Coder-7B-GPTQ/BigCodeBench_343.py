import pandas as pd
import matplotlib.pyplot as plt
COLORS = ['r', 'g', 'b', 'y', 'm']
def task_func(df, col, title=None):
    """
    Draws a pie chart of the number of unique values in a given DataFrame column with an optional title.
    
    Parameters:
    - df (pd.DataFrame): The DataFrame containing the data.
    - col (str): The column name for which to create the pie chart.
    - title (str, optional): The title of the pie chart. Defaults to None.
    
    Returns:
    - Axes: A matplotlib axes object representing the pie chart.
    """
    # Check if the input is a DataFrame and is not empty
    if not isinstance(df, pd.DataFrame) or df.empty:
        raise ValueError("Input df must be a non-empty DataFrame.")
    
    # Check if the specified column exists in the DataFrame
    if col not in df.columns:
        raise ValueError(f"Column '{col}' not found in the DataFrame.")
    
    # Get the unique values and their counts
    value_counts = df[col].value_counts()
    
    # Create the pie chart
    fig, ax = plt.subplots()
    ax.pie(value_counts, labels=value_counts.index, colors=COLORS[:len(value_counts)], autopct='%1.1f%%', startangle=140)
    
    # Set the title if provided
    if title:
        ax.set_title(title)
    
    # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.axis('equal')  
    
    return ax