
import pandas as pd
import seaborn as sns

def task_func(data):
    # Check if the DataFrame is empty
    if data.empty:
        raise ValueError("DataFrame is empty")
    
    # Filter out non-numeric columns
    numeric_data = data.select_dtypes(include=['number'])
    
    # Check if there are any numeric columns
    if numeric_data.empty:
        raise ValueError("No numeric columns present")
    
    # Calculate the cumulative sum for each column
    cumulative_sum = numeric_data.cumsum()
    
    # Create a heatmap using Seaborn
    heatmap = sns.heatmap(cumulative_sum, annot=True, fmt=".0f")
    
    # Return the Axes object
    return heatmap