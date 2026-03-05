
import pandas as pd
import matplotlib.pyplot as plt

def task_func(df, items=None, locations=None):
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
    
    # Filter the DataFrame based on the provided items and locations
    filtered_df = df[(df['Item'].isin(items)) & (df['Location'].isin(locations))]
    
    # Group by 'Item' and 'Location' and count occurrences
    count_df = filtered_df.groupby(['Item', 'Location']).size().unstack(fill_value=0)
    
    # Plotting the bar chart
    ax = count_df.plot(kind='bar', stacked=True)
    plt.xlabel('Location')
    plt.ylabel('Count')
    plt.title('Item Distribution by Location')
    plt.legend(title='Item')
    
    return ax