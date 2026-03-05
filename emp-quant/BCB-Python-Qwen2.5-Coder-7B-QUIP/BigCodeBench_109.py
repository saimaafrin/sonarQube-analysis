
import pandas as pd
import matplotlib.pyplot as plt

def task_func(df, items=None, locations=None):
    # Check if df is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("df must be a pandas DataFrame")
    
    # Check if 'Item' and 'Location' columns are in the DataFrame
    if 'Item' not in df or 'Location' not in df:
        raise ValueError("df must contain 'Item' and 'Location' columns")
    
    # If items and locations are not provided, use default lists
    if items is None:
        items = ['Item1', 'Item2', 'Item3']
    if locations is None:
        locations = ['Location1', 'Location2', 'Location3']
    
    # Filter the DataFrame based on the provided items and locations
    if items is not None:
        df = df[df['Item'].isin(items)]
    if locations is not None:
        df = df[df['Location'].isin(locations)]
    
    # Group the DataFrame by 'Location' and 'Item', then count the occurrences
    grouped = df.groupby(['Location', 'Item']).size().unstack().fillna(0)
    
    # Plot the bar chart
    fig, ax = plt.subplots()
    grouped.plot(kind='bar', ax=ax)
    ax.set_xlabel('Location')
    ax.set_ylabel('Count')
    ax.set_title('Item Distribution by Location')
    
    return ax