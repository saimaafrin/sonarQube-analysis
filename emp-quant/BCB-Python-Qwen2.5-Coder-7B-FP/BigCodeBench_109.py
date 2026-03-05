import pandas as pd
import matplotlib.pyplot as plt
def task_func(df, items=None, locations=None):
    """
    Generates a bar chart representing the distribution of specified items across given locations.
    
    Parameters:
    - df (pd.DataFrame): DataFrame containing 'Item' and 'Location' columns.
    - items (list, optional): List of items to include in the chart. Defaults to predefined list.
    - locations (list, optional): List of locations to include in the chart. Defaults to predefined list.
    
    Returns:
    - matplotlib.axes.Axes: Axes object with the plotted bar chart.
    """
    # Check if df is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("df must be a pandas DataFrame")
    
    # Check if 'Item' and 'Location' columns are present
    if 'Item' not in df.columns or 'Location' not in df.columns:
        raise ValueError("df must contain 'Item' and 'Location' columns")
    
    # Default lists if not provided
    if items is None:
        items = ['Item1', 'Item2', 'Item3']
    if locations is None:
        locations = ['LocationA', 'LocationB', 'LocationC']
    
    # Filter the DataFrame based on provided items and locations
    filtered_df = df[(df['Item'].isin(items)) & (df['Location'].isin(locations))]
    
    # Pivot the DataFrame to get the count of each item per location
    pivot_df = filtered_df.pivot_table(index='Location', columns='Item', aggfunc='size', fill_value=0)
    
    # Plot the bar chart
    ax = pivot_df.plot(kind='bar', figsize=(10, 6))
    ax.set_xlabel('Location')
    ax.set_ylabel('Count')
    ax.set_title('Item Distribution by Location')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    return ax