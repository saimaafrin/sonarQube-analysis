
import pandas as pd
import matplotlib.pyplot as plt

def task_func(df, items=None, locations=None):
    # Check if df is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input 'df' must be a pandas DataFrame.")
    
    # Check if 'Item' and 'Location' columns exist in the DataFrame
    required_columns = ['Item', 'Location']
    if not all(col in df.columns for col in required_columns):
        raise ValueError("DataFrame must contain 'Item' and 'Location' columns.")
    
    # Default lists if none are provided
    default_items = ['Apple', 'Banana', 'Cherry']
    default_locations = ['Store1', 'Store2', 'Store3']
    
    # Use default values if no specific items/locations are provided
    if items is None:
        items = default_items
    if locations is None:
        locations = default_locations
    
    # Filter the DataFrame based on the provided items and locations
    filtered_df = df[(df['Item'].isin(items)) & (df['Location'].isin(locations))]
    
    # Count occurrences of each item per location
    result = filtered_df.groupby(['Item', 'Location']).size().unstack(fill_value=0)
    
    # Plotting the bar chart
    ax = result.plot(kind='bar', figsize=(10, 6))
    ax.set_xlabel('Items')
    ax.set_ylabel('Count')
    ax.set_title('Distribution of Items Across Locations')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    return ax