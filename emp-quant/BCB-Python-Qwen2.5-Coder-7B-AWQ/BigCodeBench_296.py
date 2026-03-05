import pandas as pd
import matplotlib.pyplot as plt
def task_func(df):
    """
    Draws a bar chart of the counts of each unique value in the 'value' column of a pandas DataFrame.
    
    Parameters:
    df (pd.DataFrame): The input DataFrame with a 'value' column.
    
    Returns:
    Axes: The matplotlib Axes object of the bar chart.
    
    Raises:
    ValueError: If the input is not a DataFrame.
    """
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("The input df is not a DataFrame.")
    
    # Check if the DataFrame is empty
    if df.empty:
        return plt.gca()  # Return the current Axes object
    
    # Count the occurrences of each unique value in the 'value' column
    value_counts = df['value'].value_counts()
    
    # Create a bar chart
    ax = value_counts.plot(kind='bar')
    
    # Set the title and labels
    ax.set_title('Value Distribution')
    ax.set_xlabel('Value')
    ax.set_ylabel('Count')
    
    return ax