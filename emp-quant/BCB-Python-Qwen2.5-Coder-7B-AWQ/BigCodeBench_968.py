import pandas as pd
import seaborn as sns
import numpy as np
def task_func(data):
    # Convert the input dictionary to a pandas DataFrame
    df = pd.DataFrame(data)
    
    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("The DataFrame is empty.")
    
    # Select only numeric columns
    numeric_df = df.select_dtypes(include=[np.number])
    
    # Check if there are any numeric columns
    if numeric_df.empty:
        raise ValueError("No numeric columns are present.")
    
    # Calculate the cumulative sum of each column
    cumulative_sum_df = numeric_df.cumsum()
    
    # Create a heatmap using Seaborn
    heatmap = sns.heatmap(cumulative_sum_df, annot=True, fmt=".0f", cmap='YlGnBu')
    
    # Return the Axes object of the heatmap
    return heatmap