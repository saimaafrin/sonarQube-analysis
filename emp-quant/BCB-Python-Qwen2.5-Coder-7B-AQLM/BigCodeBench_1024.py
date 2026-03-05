
import numpy as np
import pandas as pd
import seaborn as sns
# Constants
PLOT_TITLE = "Value Distribution"

def task_func(data_dict):
    # Convert dictionary to DataFrame and remove None values
    df = pd.DataFrame(list(data_dict.values()), columns=['Values']).dropna()
    
    # Check if DataFrame is empty
    if df.empty:
        return df, None
    
    # Calculate the number of bins
    num_data_points = len(df)
    num_bins = min(11, max(2, num_data_points // 2))
    
    # Calculate min and max values
    min_value = df['Values'].min()
    max_value = df['Values'].max()
    
    # Create bin edges
    bin_edges = np.linspace(min_value, max_value, num_bins + 1)
    
    # Generate histogram using seaborn
    plot = sns.histplot(df['Values'], bins=bin_edges, kde=False)
    plot.set_title(PLOT_TITLE)
    
    return df, plot