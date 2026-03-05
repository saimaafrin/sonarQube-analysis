
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(data):
    # Check if the DataFrame is empty
    if data.empty:
        raise ValueError("The DataFrame is empty.")
    
    # Filter out non-numeric columns
    numeric_data = data.select_dtypes(include=[pd.np.number])
    
    # Check if there are any numeric columns
    if numeric_data.empty:
        raise ValueError("No numeric columns are present.")
    
    # Calculate the cumulative sum of each column
    cumulative_sum = numeric_data.cumsum()
    
    # Create a heatmap of the cumulative sum
    heatmap = sns.heatmap(cumulative_sum, annot=True, fmt=".0f", cmap="YlGnBu")
    
    # Return the Axes object of the Seaborn heatmap
    return heatmap