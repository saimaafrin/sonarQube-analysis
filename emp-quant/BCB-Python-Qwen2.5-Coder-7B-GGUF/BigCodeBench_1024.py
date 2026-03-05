
import numpy as np
import pandas as pd
import seaborn as sns
# Constants
PLOT_TITLE = "Value Distribution"

def task_func(data_dict):
    # Convert dictionary to DataFrame and remove None values
    df = pd.DataFrame(list(data_dict.values()), columns=['Values']).dropna()
    
    # Check if DataFrame is empty or all values are the same
    if df.empty or df['Values'].nunique() == 1:
        return df, None
    
    # Calculate the number of bins dynamically
    num_bins = min(11, max(2, len(df) // 2))
    
    # Create evenly spaced bin edges
    bin_edges = np.linspace(df['Values'].min(), df['Values'].max(), num_bins + 1)
    
    # Generate histogram using seaborn
    plot = sns.histplot(df['Values'], bins=bin_edges, kde=False)
    plot.set_title(PLOT_TITLE)
    
    return df, plot