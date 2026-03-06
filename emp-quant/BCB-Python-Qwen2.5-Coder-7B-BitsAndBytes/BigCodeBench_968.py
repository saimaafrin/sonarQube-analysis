
import pandas as pd
import seaborn as sns
import numpy as np

def task_func(data):
    # Check if the data is empty
    if not data:
        raise ValueError("The DataFrame is empty.")
    
    # Convert the input dictionary to a DataFrame
    df = pd.DataFrame(data)
    
    # Filter out non-numeric columns
    numeric_df = df.select_dtypes(include=[np.number])
    
    # Check if there are any numeric columns
    if numeric_df.empty:
        raise ValueError("No numeric columns are present.")
    
    # Calculate the cumulative sum of each column
    cumsum_df = numeric_df.cumsum()
    
    # Create a heatmap using Seaborn
    ax = sns.heatmap(cumsum_df, annot=True, cmap='YlGnBu')
    
    return ax