
import numpy as np
import pandas as pd
import seaborn as sns

# Constants
PLOT_TITLE = "Value Distribution"

def task_func(data_dict):
    # Convert dictionary to DataFrame and remove None values
    df = pd.DataFrame(list(data_dict.items()), columns=['Key', 'Value']).dropna(subset=['Value'])
    
    # Check if DataFrame is empty
    if df.empty:
        return df, None
    
    # Remove duplicates to ensure variability
    df = df.drop_duplicates(subset='Value')
    
    # Check if all values are the same
    if df['Value'].nunique() == 1:
        return df, None
    
    # Calculate min and max values
    min_val = df['Value'].min()
    max_val = df['Value'].max()
    
    # Determine the number of bins
    num_bins = min(11, max(2, len(df) // 2))
    
    # Generate histogram
    ax = sns.histplot(data=df, x='Value', bins=num_bins, kde=False)
    ax.set_title(PLOT_TITLE)
    
    return df, ax